import json
from src.class_abstract import BaseJson

class JSONSaver(BaseJson):
    """
    Класс для работы с файлами: сохранение и чтение данных в формате JSON
    """

    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def save_data(self, data):
        """Сохраняет данные в JSON-файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read_data(self):
        """Читает данные из JSON-файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_vacancy(self):
        pass

    def delete_vacancy(self):
        pass