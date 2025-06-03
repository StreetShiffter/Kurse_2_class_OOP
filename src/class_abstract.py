from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseApi(ABC):
    """Базовый абстрактный клас для API методов"""
    @property
    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class BaseJSON(ABC):
    """Абстрактный класс для работы с файлами или хранилищами данных"""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """Добавить вакансию"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Получить список вакансий по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, criteria: Dict[str, Any]) -> None:
        """Удалить вакансию по критерию"""
        pass