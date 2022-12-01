import mysql.connector
import json
from flask import make_response, jsonify
from flask import make_response
from configs.config import dbconfig
from datetime import datetime, timedelta
class user_model():
    def __init__(self): #constructor
        try: #try & except for exception handling
        #connection code
            self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            #self. use kore amra con,cur variable gula k globally define kore dilam
            #dictionary is like {"raad":"2243"}
            #cursor is like an agent that will help to traverse anywhere
            print("Connected with Database")
        except:
            print("Could not connect to server")    

            
    
    def loginapi(self, data):
        self.cur.execute(f"SELECT * from user WHERE u_email='{data['u_email']}'")
        login = self.cur.fetchall() #storing all data in result
        if len(login)>0:
            res = make_response({"User Login Data": login},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No data Found"    

    def forgetpassword(self, data):
        self.cur.execute(f"UPDATE user SET u_pass='{data['u_pass']}' WHERE u_email='{data['u_email']}'")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)


    def fooddata(self, data):
        self.cur.execute(f"SELECT id, food_id, food_name, res_id, res_name, food_price, food_category, food_pos_cat, food_photo, food_detail, food_variation, food_discount, food_coupon, food_rating, food_active FROM food WHERE res_id='{data['res_id']}'")
        result = self.cur.fetchall() #storing all data in result
        if len(result)>0:
            res = make_response({"Food Data": result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No data Found"

    def foodsearch(self, data):
        self.cur.execute(f"SELECT id, food_id, food_name, res_id, res_name, food_price, food_category, food_pos_cat, food_photo, food_detail, food_variation, food_discount, food_coupon, food_rating, food_active FROM food WHERE res_id='{data['res_id']}' and food_name like'%{data['food_name']}%'")
        result = self.cur.fetchall() #storing all data in result
        if len(result)>0:
            res = make_response({"Food Name Wise Search Data": result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No Food Found"

    def foodcategorysearch(self, data):
        self.cur.execute(f"SELECT id, food_id, food_name, res_id, res_name, food_price, food_category, food_pos_cat, food_photo, food_detail, food_variation, food_discount, food_coupon, food_rating, food_active FROM food WHERE res_id='{data['res_id']}' and food_category='{data['food_category']}'")
        categoryw = self.cur.fetchall() #storing all data in result
        if len(categoryw)>0:
            res = make_response({"Category Wise Search Data": categoryw},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No Categories Found"

    def foodcategorydatafetch(self, data):
        self.cur.execute(f"SELECT food_category FROM food WHERE res_id='{data['res_id']}'")
        categoryfetch = self.cur.fetchall() #storing all data in result
        if len(categoryfetch)>0:
            res = make_response({"Available Categories": categoryfetch},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No Categories Found"

# REMAINING PLACE ORDER FUNCTIONS
    #search order
    def checkorder(self, data):
        self.cur.execute(f"SELECT * FROM orderd WHERE cart_id='{data['cart_id']}'")
        categoryfetch = self.cur.fetchall() #storing all data in result
        if len(categoryfetch)>0:
            res = make_response({"Order Details": categoryfetch},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No Order Found"
    #update order
    def editorder(self, data):
        self.cur.execute(f"UPDATE orderd SET food_quantity='{data['food_quantity']}',food_price='{data['food_price']}',tot_price='{data['tot_price']}',variation='{data['variation']}',delivery_status='{data['delivery_status']}',created_at='NOW()' WHERE cart_id='{data['cart_id']}' and res_id='{data['res_id']}'")
        if self.cur.rowcount>0:
            return make_response({"message":"ORDER UPDATED SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)
   #Today Report
    def todayreport(self, data):
        self.cur.execute(f"SELECT SUM(tot_amount) as totaltk,COUNT(orderm_id) as totalorders,COUNT(user_id) as customer,orderm_id, user_id, cart_id, tot_amount, purchase_type, payment_type, date_time FROM orderm WHERE date_time between concat(curdate(),' ','00:00:00') AND concat(curdate(),' ','23:59:59') and payment_type='{data['payment_type']}'")
        categoryfetch = self.cur.fetchall() #storing all data in result
        if len(categoryfetch)>0:
            res = make_response({"Sales Report Details": categoryfetch},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return "No Sales Report Found"

# Food Items


    def foodentry(self, data): #food photo is not inserted here
        self.cur.execute(f"INSERT INTO food(id, food_id, food_name, res_id, res_name, food_price, food_category, food_pos_cat,  food_detail, food_variation, food_discount, food_coupon, food_rating, food_active) VALUES ('{data['id']}','{data['food_id']}','{data['food_name']}','{data['res_id']}','{data['res_name']}','{data['food_price']}','{data['food_category']}','{data['food_pos_cat']}','{data['food_detail']}','{data['food_variation']}','{data['food_discount']}','{data['food_coupon']}','{data['food_rating']}','{data['food_active']}')")
        return "Food Inserted"