from pymongo import MongoClient
from dev_vacancies.destination_collection import Extract


def load_data_to_collection(data, collection_name):
    for el in data:
        text_for_vacancy, link_to_vacancy, company_name = el
        collection_name.update_one({'company': company_name}, {'$addToSet': {
            'vacancies': {'summary': text_for_vacancy,
                          'link': link_to_vacancy}}}, True)


if __name__ == '__main__':
    client = MongoClient()
    extract_obj = Extract()

    db = client.vacancies
    col = db.vacancies_tmp

    data = extract_obj.get_data()
    load_data_to_collection(data, col)
