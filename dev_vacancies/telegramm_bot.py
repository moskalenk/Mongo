import requests


def send_message(company_name, link):
    BOT_TOKEN = 'bot463746687:AAGziRJXirlhHGqRNr5hdfJslvb8BlBet6A'
    CHAT_ID = '314673497'
    init_text = 'Новая вакансия, глянь!'

    requests.post(
        f'https://api.telegram.org/{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&'
        f'text={init_text}\n\n'
        f'Компания - *{company_name}*\n\n'
        f'{link}&parse_mode=markdown').raise_for_status()
