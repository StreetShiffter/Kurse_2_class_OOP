import json
from abc import ABC, abstractmethod

from src.class_api import HeadHunterAPI
from src.class_vacancy_worker import Vacancy
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(script_dir, "../data/vacancies.json")

class AbstractSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria=None):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractSaver):
    def __init__(self, filename=path_to_json):
        self.__filename = filename

    def add_vacancy(self, vacancy):
        data = self.get_vacancies() or []
        if not any(v["link"] == vacancy.link for v in data):
            data.append(
                {
                    "name": vacancy.name,
                    "link": vacancy.link,
                    "salary_from": vacancy.salary_from,
                    "salary_to": vacancy.salary_to,
                    "description": vacancy.description,
                }
            )
            with open(self.__filename, "a", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self, criteria=None):
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
        if criteria is None:
            return data
        filtered = []
        for v in data:
            match = True
            for key, value in criteria.items():
                if key not in v or value.lower() not in str(v[key]).lower():
                    match = False
                    break
            if match:
                filtered.append(v)
        return filtered

    def delete_vacancy(self, vacancy):
        data = self.get_vacancies() or []
        data = [v for v in data if v["url"] != vacancy.link]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    api = HeadHunterAPI()
    vacancies_json = api.get_vacancies(text="Python", per_page=15)
    print(f"Найдено вакансий: {len(vacancies_json)}")

    vacancies = Vacancy.cast_to_object_list(vacancies_json)

    for vac in vacancies:
        print(f"Название: {vac.name}")
        print(f"Ссылка: {vac.link}")
        print(f"Зарплата: {vac.salary_from} - {vac.salary_to}")
        print(f"Описание: {vac.description}")
        print("-" * 40)

    vaci = {
        "name": "Программист дебил",
        "link": "https://api.hh.su",
        "area": "Долбоебск",
        "salary_from": 150,
        "salary_to": 200,
        "description": "БЫТЬ ЕБЛАНОМ"
    }

    # saver = JSONSaver(path_to_json)
    # for vac in vacancies:
    #     saver.add_vacancy(vaci)

    # for vac in vacancies:
    #     saver.delete_vacancy(vac)