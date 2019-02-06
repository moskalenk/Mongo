from pymongo import MongoClient
import pymongo.errors
from telegramm_bot import send_message


def main():
    try:
        with col.watch([{'$match': {'operationType': 'insert', 'fullDocument.message':{'$exists': 0}}}]) as stream:
            for insert_change in stream:
                changes = insert_change
                company_name = changes['fullDocument']['company']
                vacancy_link = changes['fullDocument']['vacancies'][0]['link']

                send_message(company_name, vacancy_link)
    except pymongo.errors.PyMongoError:
        pass


if __name__ == '__main__':
    client = MongoClient(port=27100)

    db = client.vacancies
    col = db.destination_collection

    main()
