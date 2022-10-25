from application import app
from flask import jsonify, session
#from flask_cors import CORS,cross_origin
#CORS(app, supports_credentials=True)


@app.route('/sampleapi/')
def test_backend():
    #db.users.insert_one({"name":"Amaechi Tochukwu"})
    return {
        "members":["Amaechi","Sandra","Cynthia"]
    }