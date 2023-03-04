from pprint import pprint
from pymongo import MongoClient
import time
from datetime import datetime
import random


client = MongoClient('localhost', port=27017)

db = client["stream"]
coll = db["incoming"]

n = 5

while True:
    time.sleep(n)
    new_document_id = coll.insert_one({"author": "Balint", "timestamp": datetime.now(), "message": "test"}).inserted_id
    pprint(coll.find_one({"_id": new_document_id}))
    n = random.randint(1, 10)

