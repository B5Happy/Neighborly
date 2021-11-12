import os

class Config(object):
    localhost = os.environ.get('localhost') or 'mongodb://udacity2project:Pb4d2coWkxvSmqQ7iv0H9aVRhmXMWYxIKE61asVJNx2gsNuFTltMIsKz3v07XXsu14HENUlVxnG3h71xMOcw3A==@udacity2project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@udacity2project@'
    database = os.environ.get('BLOB_ACCOUNT') or 'myneighborlydb'
    collectionAds = os.environ.get('collectionAds') or 'ads'
    collectionPosts = os.environ.get('collectionPosts') or 'posts'
