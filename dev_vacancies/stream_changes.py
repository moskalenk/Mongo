from pymongo import MongoClient
import pymongo.errors

client = MongoClient()

db = client.vacancies
col = db.vacancies_test

try:
    with db.vacancies_test.watch([{'$match': {'operationType': 'insert', 'fullDocument.message':{'$exists':0}}}]) as stream:
        for insert_change in stream:
            print(insert_change)
            db.test.insert({'message':'Hello from python!_2'})
            # db.test.insert(insert_change["fullDocument"])
            # db.another.update({"_id": insert_change["documentKey"]["_id"]}, {"$set":{"from_python": "hello"}})
except pymongo.errors.PyMongoError:
    pass