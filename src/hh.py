from typing import Any, Optional


class Vacancy:
    """Класс для обработки вакансий"""

    __slots__ = (
        "id",
        "name",
        "link",
        "area",
        "__salary",
        "description",
        "salary_from",
        "salary_to",
    )

    def __init__(
        self,
        id: int,
        name: str,
        link: str,
        salary: Optional[dict[str, Any]],
        area: str,
        description: str,
    ):
        self.id = id
        self.name = name
        self.link = link
        self.area = area
        self.__salary = salary
        self.description = description
        self.salary_from = self.__validate_salary_from()
        self.salary_to = self.__validate_salary_to()
        # self.__get_salary()

    def __validate_salary_from(self) -> int:
        """Валидация данных по зарплате для поля 'от'"""
        self.salary_from = 0
        if self.__salary:  # если есть данные о зарплате
            self.salary_from = self.__salary.get("from") or 0

            # переводим в целые числа при необходимости
            try:
                self.salary_from = int(self.salary_from)
            except (TypeError, ValueError):
                self.salary_from = 0
        return self.salary_from

    def __validate_salary_to(self) -> int:
        """Валидация данных по зарплате для поля 'до'"""
        self.salary_to = 0
        if self.__salary:  # если есть данные о зарплате
            self.salary_to = self.__salary.get("to") or 0

            # переводим в целые числа при необходимости
            try:
                self.salary_to = int(self.salary_to)
            except (TypeError, ValueError):
                self.salary_to = 0
        return self.salary_to

    # def __get_salary(self) -> None:
    #     """Обработка данных о зарплате"""
    #     self.salary_from = 0
    #     self.salary_to = 0
    #
    #     if self.__salary:  # если есть данные о зарплате
    #         self.salary_from = self.__salary.get("from") or 0
    #         self.salary_to = self.__salary.get("to") or 0
    #
    #         # переводим в целые числа при необходимости
    #         try:
    #             self.salary_from = int(self.salary_from)
    #             self.salary_to = int(self.salary_to)
    #         except (TypeError, ValueError):
    #             self.salary_from = 0
    #             self.salary_to = 0

    def __gte__(self, other):
        """Сравнение зарплат"""
        if self.salary_from >= other.salary_from:
            return self.salary_from

    def __lte__(self, other):
        """Сравнение зарплат"""
        if self.salary_from <= other.salary_from:
            return self.salary_from

    def as_dict(self) -> dict[str, Any]:
        """Представление данных в виде словаря"""
        # salary_data = {}
        # if self._salary:
        #     salary_data["salary"] = self._salary
        # if self.salary_from > 0:
        #     salary_data["salary_from"] = self.salary_from
        # if self.salary_to > 0:
        #     salary_data["salary_to"] = self.salary_to

        result = {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "area": self.area,
            "description": self.description,
            # **salary_data,
        }

        if self.salary_from > 0:
            result["salary_from"] = self.salary_from
        if self.salary_to > 0:
            result["salary_to"] = self.salary_to

        return result

    def __str__(self):
        """Представление для объектов класса Vacancy"""
        return (
            f"Vacancy(id={self.id}, name ='{self.name}', salary_from={self.salary_from}, "
            f"salary_to={self.salary_to}, link='{self.link}')"
        )

    def __repr__(self):
        return self.__str__()