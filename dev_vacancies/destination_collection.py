from dev_vacancies import draft_collections
from dev_vacancies.constants import MAIN_URL


def get_all_companies_name():
    list_jobs = draft_collections.getting_audit_data()
    return list_jobs.find_all('strong')


def get_summary_and_link():
    list_jobs = draft_collections.getting_audit_data()
    all_h3 = list_jobs.find_all('h3')

    for h3 in all_h3:
        a = h3.find('a')
        link_to_vacancy = MAIN_URL + a['href']
        text_for_vacancy = a.text
        yield text_for_vacancy, link_to_vacancy


def get_company_name():
    company_name = get_all_companies_name()
    for company in company_name:
        name = company.text
        yield name.strip()


def get_data():
    for el in map(lambda x, y: [x, y], get_summary_and_link(), get_company_name()):
        text_for_vacancy = el[0][0]
        link_to_vacancy = el[0][1]
        company_name = el[1]

        yield text_for_vacancy, link_to_vacancy, company_name
