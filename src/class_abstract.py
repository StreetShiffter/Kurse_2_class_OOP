from abc import ABC, abstractmethod

class BaseApi(ABC):
    """Базовый абстрактный клас для API методов"""
    @property
    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

class BaseVacancy(ABC):
    @abstractmethod
    def cast_to_object_list(self):
        pass


class BaseJson(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass