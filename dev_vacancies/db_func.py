from pymongo import MongoClient

client = MongoClient()

db = client.vacancies
# col = db.vacancies_new
col = db.vacancies_test

# first_post = {
#   "company_name": [
#     {"ISsoft": [
#       {"QA": "link"}
#     ],
#       "Yandex": [
#         {"QA_Auto": "link_1"},
#         {"QA_Maschine": "link_2"}
#       ]}
#   ]
# }

link = 'https://dev.by/news/play2live-ne-zaplatil-sotrudnikam'

is_soft_post = {
  "ISsoft": [
    {"QA": "link"}
  ]
}

yandex_post = {
  "Yandex": [
    {"QA_Auto": "link_1"},
    {"QA_Maschine": link}
  ]
}

ls = [is_soft_post, yandex_post]
# post_id = col.insert_one(yandex_post)
post_id = col.insert_many([x for x in ls])