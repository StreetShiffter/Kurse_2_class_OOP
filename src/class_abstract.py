from abc import ABC, abstractmethod

class BaseApi(ABC):
    """Базовый абстрактный клас для API методов"""

    @abstractmethod
    def response_check(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass