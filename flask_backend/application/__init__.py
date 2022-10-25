from flask import Flask
from flask_pymongo import PyMongo
from application import config
from flask_cors import CORS,cross_origin


app=Flask(__name__, instance_relative_config=True)
CORS(app, supports_credentials=True)

app.config.from_pyfile("config.py")
app.config.from_object(config.ApplicationSettings)

#mongodb_client=PyMongo(app)
#db=mongodb_client.db

from application.routes import user_routes