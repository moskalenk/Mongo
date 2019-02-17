import requests
from bs4 import BeautifulSoup

from dev_vacancies.constants import VACANCY_URL


def get_response(url):
    return requests.get(url)


def getting_staging_data():
    vacancies_page = get_response(VACANCY_URL)
    return BeautifulSoup(vacancies_page.text, 'html.parser')


def getting_audit_data():
    soup = getting_staging_data()
    list_jobs = soup.find(class_='list-jobs')
    return list_jobs
