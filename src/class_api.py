import requests
from config import USER_AGENT
from src.class_abstract import BaseApi
from src.class_json import JSONSaver
import pprint
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(script_dir, "../data/vacancy_result.json")


class HeadHunterAPI(BaseApi) :
    """Метод запроса через API"""

    def __init__(self, url) -> None:
        self.__url = url


    @property
    def url(self) -> None:
        """Метод получение приватного атрибута"""
        return self.__url

    def __response_check(self) -> bool:
        """Проверяет доступность API"""
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status() #if status_code == 200
            return True
        except requests.exceptions.RequestException:
            return False

    def get_vacancies(self, text: str, per_page: int = 10) -> list[dict]:
        if not self.__response_check():
            raise ConnectionError("API недоступно. Невозможно получить вакансии.")

        headers = {'User-Agent': USER_AGENT}
        params = {'text': text, 'per_page': per_page}
        try:
            response = requests.get(self.url, headers=headers, params=params)
            response.raise_for_status()  # Если код будет 200
            return response.json().get('items', [])  # получение items если найдет( или [] )
        except requests.exceptions.RequestException as e:  # отлов только сетевых ошибок
            raise ValueError(f"Ошибка при выполнении запроса: {e}") from e  # Сохранить историю ошибки from e


# if __name__ == "__main__":
#     test = "https://api.hh.ru/vacancies"
#
#     load = HeadHunterAPI(test)  # создаем объект API
#     result = load.get_vacancies('Строитель')# получен json
# # #     record = JSONSaver(path_to_json)  # создаем объект для функций работы json
# # #     result_2 = record.save_data(result)  # записываем полученный json
# # #params = {'text': 'python', 'page': 1, 'per_page': 3}
# # #     print(result_2)
#     pprint.pprint(len(result))
