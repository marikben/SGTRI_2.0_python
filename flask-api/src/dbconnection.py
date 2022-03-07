from flask import Flask, request
from flask_restful import Api, Resource
from model import Project
from flask_pymongo import PyMongo
from pymongo.collection import Collection, ReturnDocument
import fastapi

from fastapi.encoders import jsonable_encoder

from objectid import PydanticObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mariam:cocktail@cocktails.xvbgt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)
api = Api(app)

collectionnames: Collection = mongo.db.collections

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cocktails/", methods=["POST"])
def new_cocktail():
    raw_cocktail = request.get_json()
    raw_cocktail["date_added"] = datetime.utcnow()

    cocktail = Cocktail(**raw_cocktail)
    insert_result = collections.insert_one(cocktail.to_bson())
    cocktail.id = PydanticObjectId(str(insert_result.inserted_id))
    print(cocktail)

    return cocktail.to_json()

if __name__ == '__main__':
    app.run()

