from pymongo import MongoClient
import pymongo.errors
from main_page import Common

client = MongoClient()
vac_obj = Common()

db = client.vacancies
col = db.vacancies_tmp

count = 0

for vac in vac_obj.get_data():
  text_for_vacancy, link_to_vacancy, company_name = vac

  col.update_one({'company': company_name}, {'$addToSet': {'vacancies': {'summary': text_for_vacancy, 'link': link_to_vacancy}}}, True)

# try:
#     with db.vacancies_test.watch([{'$match': {'operationType': 'insert', 'fullDocument.message':{'$exists':0}}}]) as stream:
#         for insert_change in stream:
#             print(insert_change)
#             db.test.insert({'message':'Hello from python!_2'})
#             # db.test.insert(insert_change["fullDocument"])
#             # db.another.update({"_id": insert_change["documentKey"]["_id"]}, {"$set":{"from_python": "hello"}})
# except pymongo.errors.PyMongoError:
#     pass