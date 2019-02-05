from pymongo import MongoClient
import pymongo.errors

client = MongoClient(port=27100)

db = client.vacancies
col = db.vacancies_tmp


try:
    with col.watch([{'$match': {'operationType': 'insert', 'fullDocument.message':{'$exists':0}}}]) as stream:
        for insert_change in stream:
            print(insert_change)
except pymongo.errors.PyMongoError:
    pass

