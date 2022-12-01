from flask import Flask 

# from gevent.pywsgi import WSGIServer
# import request, json, jsonify
# from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['DEBUG'] = True


# if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    # http_server = WSGIServer(('103.150.48.234', 2164), app)
    # http_server.serve_forever()
# @app.route("/")
# def raad():  #created a function
#     return "Raad"

# @app.route("/home")
# def welcome():  #created a function
#     return "Welcome"

from controller import * 
#for differnet file will use comma