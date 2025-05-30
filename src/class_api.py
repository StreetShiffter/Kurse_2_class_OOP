import requests
from config import USER_AGENT
from src.class_abstract import BaseApi
from src.class_json import JSONSaver
import pprint
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(script_dir, "../data/vacancy_result.json")


class HeadHunterAPI(BaseApi):
    def __init__(self, url):
        self.url = "https://api.hh.ru/vacancies"

    def response_check(self):
        response = requests.get(self.url)
        return response

    def get_vacancies(self, params: dict) -> None :
        self.headers = USER_AGENT
        self.params = {'text':'python','page': 1,'per_page' : 3}
        headers = {'User-Agent' : self.headers}
        response = requests.get(self.url, headers = headers, params = params)
        if not response:
            raise ValueError(f'Запрос {response} недоступен!')
        data = response.json()
        return data

if __name__ == "__main__":
    test = "https://api.hh.ru/vacancies"
    params = {'text':'python','page': 1,'per_page' : 3}

    load = HeadHunterAPI(test)# создаем объект API
    result = load.get_vacancies(params)# получен json
    record = JSONSaver(path_to_json) # создаем объект для функций работы json
    result_2 = record.save_data(result) # записываем полученный json
    print(result_2)
    pprint.pprint(result)