from flask import Flask, request
from flask_restful import Api, Resource
from model import Collection
from flask_pymongo import PyMongo
from pymongo.collection import Collection, ReturnDocument
import fastapi

from fastapi.encoders import jsonable_encoder

from objectid import PydanticObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mariam:cocktail@cocktails.xvbgt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)
api = Api(app)

collections: Collection = mongo.db.collections

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/documents/", methods=["POST"])
def new_doc():
    raw_doc = request.get_json()
    doc = Collection(**raw_doc)
    insert_result = collections.insert_one(doc.to_bson())
    doc.id = PydanticObjectId(str(insert_result.inserted_id))
    print(doc)

    return doc.to_json()

if __name__ == '__main__':
    app.run()

