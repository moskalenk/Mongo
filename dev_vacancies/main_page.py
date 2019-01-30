import requests
from bs4 import BeautifulSoup

MAIN_URL = 'https://jobs.dev.by'

vacancies_page = requests.get('https://jobs.dev.by/?search-jobs[user_type_of_activity]=3&search-jobs-filter=true')

soup = BeautifulSoup(vacancies_page.text, 'html.parser')
list_jobs = soup.find(class_='list-jobs')
all_h3 = list_jobs.find_all('h3')

company_name = list_jobs.find_all('strong')
# company_name = list_jobs.find('strong')
# print(company_name.text)


def get_data():
    for h3 in all_h3:
        for company in company_name:
            name = company.text

            a = h3.find('a')
            link_to_vacancy = MAIN_URL + a['href']
            text_for_vacancy = a.text

            yield f'{link_to_vacancy} - {text_for_vacancy} - {name.strip()}'


res = get_data()
print(list(res))
