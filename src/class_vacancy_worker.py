import json
from typing import Any, Dict, List

# import pprint
# from src.class_api import HeadHunterAPI
from src.utils import json_load


class Vacancy:
    """Класс для обработки вакансий"""

    __slots__ = (
        "name",
        "id",
        "area",
        "__salary",
        "description",
        "salary_from",
        "salary_to",
    )

    def __init__(self, name: str, id: str, salary: dict[str, int, float], area: str, description: str) -> None:

        self.name = name
        self.id = id

        # Если area — это словарь (например, из API), берём 'name'
        if isinstance(area, dict):
            self.area = area.get("name", "Не указано")
        else:
            self.area = area or "Не указано"

        self.__salary = salary  # Зарплата подробно в словаре
        self.description = description
        self.salary_from = self.__salary_from()  # Валидируем строку от из словаря
        self.salary_to = self.__salary_to()  # Валидируем строку до из словаря

    def __salary_from(self) -> int:
        """Валидация данных по зарплате для поля 'от'"""
        self.salary_from = 0
        if self.__salary:  # если есть данные о зарплате
            self.salary_from = self.__salary.get("from") or 0

            try:
                self.salary_from = int(self.salary_from)
            except (TypeError, ValueError):
                self.salary_from = 0
        return self.salary_from

    def __salary_to(self) -> int:
        """Валидация данных по зарплате для поля 'до'"""
        self.salary_to = 0
        if self.__salary:  #
            self.salary_to = self.__salary.get("to") or 0

            try:
                self.salary_to = int(self.salary_to)
            except (TypeError, ValueError):
                self.salary_to = 0
        return self.salary_to

    def __str__(self) -> str:
        """Метод преобразования атрибутов в строку и вывод в консоль"""

        return (
            f"Вакансия: {self.name}\n"
            f"Id вакансии: {self.id}\n"
            f"Расположение: {self.area}\n"
            f"Описание: {self.description}\n"
            f"Зарплата от: {self.salary_from}\n"
            f"Зарплата до: {self.salary_to}\n"
            "--------------------------"
        )

    def __ge__(self, other: Any) -> bool:
        """Методы сравнения конкретных вакансий"""
        if not isinstance(other, Vacancy):
            raise AttributeError("Невозможно сравнить разные типы")
        return self.salary_from >= other.salary_from

    def __le__(self, other: Any) -> bool:
        """Методы сравнения конкретных вакансий"""
        if not isinstance(other, Vacancy):
            raise AttributeError("Невозможно сравнить разные типы")
        return self.salary_from <= other.salary_from

    def __gt__(self, other: Any) -> bool:
        """Методы сравнения конкретных вакансий"""
        if not isinstance(other, Vacancy):
            raise AttributeError("Невозможно сравнить разные типы")
        return self.salary_from > other.salary_from

    def __lt__(self, other: Any) -> bool:
        """Методы сравнения конкретных вакансий"""
        if not isinstance(other, Vacancy):
            raise AttributeError("Невозможно сравнить разные типы")
        return self.salary_from < other.salary_from

    @staticmethod
    def cast_to_object_list(data: List[Dict[str, Any]]) -> List["Vacancy"]:
        """Преобразует список JSON-объектов в список объектов Vacancy."""
        vacancy_list = []

        for item in data:
            try:
                name = item.get("name")
                id = item.get("id")

                area = item.get("area", {})  # передаем весь объект area

                snippet = item.get("snippet", {})
                responsibility = snippet.get("responsibility")
                description = responsibility or item.get("description", "")

                salary = item.get("salary", {})

                # Создание объекта Vacancy
                vacancy = Vacancy(name=name, id=id, area=area, salary=salary, description=description)
                vacancy_list.append(vacancy)

            except Exception as e:
                print(f"Ошибка при обработке вакансии: {e}")
                continue

        return vacancy_list

    @staticmethod
    def sort_vacancies_by_salary(vacancies: list["Vacancy"], reverse: bool = True) -> list["Vacancy"]:
        """Сортировка списка вакансий по зарплате (по возрастанию или убыванию)"""
        return sorted(vacancies, key=lambda v: v.salary_from, reverse=reverse)

    def to_dict(self) -> dict:
        """Преобразует объект Vacancy в словарь для сериализации в JSON"""
        return {
            "name": self.name,
            "id": self.id,
            "area": self.area,
            "salary": self.__salary,  # Сохраняем оригинальный словарь с зарплатой
            "description": self.description,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
        }

    @staticmethod
    def load_from_json(filename: str) -> List["Vacancy"]:
        """Загружает список вакансий из JSON-файла обратно в объекты Vacancy"""
        try:
            data = json_load(filename)

            vacancies = []
            for item in data:
                vacancy = Vacancy(
                    name=item["name"],
                    id=item["id"],
                    area=item["area"],
                    salary=item["salary"],
                    description=item["description"],
                )
                vacancies.append(vacancy)
            return vacancies

        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка при чтении JSON из файла {filename}.")
            return []


# if __name__ == "__main__":
#     hh_api = HeadHunterAPI() # создаем объект API
#     data = hh_api.get_vacancies("Python разработчик")
#     vacancies_list = Vacancy.cast_to_object_list(data)
#     print("Преобразованные вакансии:", vacancies_list)  # DEBUG
#     vacancy = Vacancy('Плотник',
#                       'https://api.hh.ru/areas/1',
#                       {'from': 5000000, 'to': 180000, 'currency': 'RUR'},
#                       "Москва",
#                       "Выполнение столярно-плотницких работ")
#
#     print(vacancy.area)
# pprint.pprint(vacancies)

# vacancies = Vacancy.cast_to_object_list(data)
# if len(vacancies) >= 2:
#     if vacancies[0] > vacancies[9]:
#         print("Вакансия 0 лучше вакансии 1")
#     elif vacancies[0] < vacancies[1]:
#         print("Вакансия 1 лучше вакансии 0")
#     else:
#         print("Зарплаты равны")
# else:
#     print("Недостаточно вакансий для сравнения")

# # Сортируем по возрастанию зарплаты
# sorted_vacancies_asc = Vacancy.sort_vacancies_by_salary(vacancies)
#
# # Сортируем по убыванию зарплаты
# sorted_vacancies_desc = Vacancy.sort_vacancies_by_salary(vacancies, reverse=False)
#
# # Выводим результат
# for vacancy in sorted_vacancies_desc:
#     print(vacancy)


# @classmethod
# def from_dict(cls, data: dict):
#     return cls(
#         name=data.get("name"),
#         link=data.get("link"),
#         area=data.get("area"),
#         salary={"from": data.get("salary_from"), "to": data.get("salary_to")},
#         description=data.get("description")
#     )
#
# # В class Vacancy:
# def to_dict(self) -> dict:
#     return {
#         "name": self.name,
#         "link": self.link,
#         "area": self.area,
#         "salary_from": self.salary_from,
#         "salary_to": self.salary_to,
#         "description": self.description
#     }

# @staticmethod
# def save_to_json(vacancies: List["Vacancy"], filename: str) -> None:
#     """Сохраняет список вакансий в JSON-файл"""
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump([vac.to_dict() for vac in vacancies], f, ensure_ascii=False, indent=4)
#     print(f"Сохранено {len(vacancies)} вакансий в файл {filename}")

# @staticmethod
# def filter_vacancies(vacancies: list["Vacancy"], reverse: bool = True) -> list["Vacancy"]:
#     """Фильтрация списка вакансий по слову"""
#     return sorted(vacancies, key=lambda v: v.salary_from, reverse=reverse)
