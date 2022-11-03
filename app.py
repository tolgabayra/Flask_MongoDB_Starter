import os
from flask import Flask
from flask_cors import CORS
from controller.coffee_controller import coffee_route
from mongoengine import connect

app = Flask(__name__)
CORS(app)

app.register_blueprint(coffee_route)

connect(host=os.environ.get('MONGO_URL'))

if __name__=="__main__":
    app.debug = True
    app.run(host="http://localhost")