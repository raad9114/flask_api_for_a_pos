from app import app
from model.user_model import user_model
from flask import request

object = user_model()

@app.route("/foodentry", methods=["POST"])
def foodentry():
    return object.foodentry(request.json)

@app.route("/login", methods=["POST"])
def loginapi():
    return object.loginapi(request.json)    

@app.route("/forgetpass", methods=["PUT"])
def forgetpassword():
    return object.forgetpassword(request.json)    

@app.route("/fooddata", methods=["POST"])
def fooddata():
    return object.fooddata(request.json)

@app.route("/foodsearching", methods=["POST"])
def foodsearch():
    return object.foodsearch(request.json)

@app.route("/categoryfetch", methods=["POST"])
def foodcategorydatafetch():
    return object.foodcategorydatafetch(request.json)


