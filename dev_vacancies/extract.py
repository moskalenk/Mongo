import requests
from bs4 import BeautifulSoup


class Extract:

    MAIN_URL = 'https://jobs.dev.by'

    vacancies_page = requests.get('https://jobs.dev.by/?search-jobs[user_type_of_activity]=3&search-jobs-filter=true')

    soup = BeautifulSoup(vacancies_page.text, 'html.parser')
    list_jobs = soup.find(class_='list-jobs')
    all_h3 = list_jobs.find_all('h3')

    company_name = list_jobs.find_all('strong')

    def get_summary_and_link(self):
        for h3 in self.all_h3:
            a = h3.find('a')
            link_to_vacancy = self.MAIN_URL + a['href']
            text_for_vacancy = a.text
            yield text_for_vacancy, link_to_vacancy

    def get_company_name(self):
        for company in self.company_name:
            name = company.text
            yield name.strip()

    def get_data(self):
        for el in map(lambda x, y: [x, y], self.get_summary_and_link(), self.get_company_name()):
            text_for_vacancy = el[0][0]
            link_to_vacancy = el[0][1]
            company_name = el[1]

            yield text_for_vacancy, link_to_vacancy, company_name
