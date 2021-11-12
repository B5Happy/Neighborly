import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from config import Config

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = Config.localhost
        client = pymongo.MongoClient(url)
        database = client[Config.database]
        collection = database[Config.collectionAds]


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

