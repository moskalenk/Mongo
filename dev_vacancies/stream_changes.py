from pymongo import MongoClient
import pymongo.errors

client = MongoClient()

db = client.vacancies
col = db.vacancies_test

try:
    with col.watch(
            [{'$match': {'operationType': 'insert'}}]) as stream:
        for insert_change in stream:
            print(insert_change)
except pymongo.errors.PyMongoError:
    pass
