import azure.functions as func
import pymongo
from bson.objectid import ObjectId
from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = Config.localhost
            client = pymongo.MongoClient(url)
            database = Config.database
            collection = Config.collectionAds
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
