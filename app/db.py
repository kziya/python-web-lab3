import os
from pymongo import MongoClient

connection = MongoClient(os.getenv('MONGO_URI'))


def get_db():
    return connection['main']



