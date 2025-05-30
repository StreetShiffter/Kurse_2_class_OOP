import requests
import json


class JSONFileWorker:
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


class Parser:
    """
    Базовый класс парсера
    """

    def __init__(self, file_worker):
        self.file_worker = file_worker


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/self'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """Загружает вакансии по ключевому слову"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:  # Загружаем до 20 страниц
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json().get('items', [])
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                print("Ошибка при загрузке данных:", response.status_code)
                break

        # Сохраняем результат в файл
        self.file_worker.save_data(self.vacancies)
        print(f"Загружено {len(self.vacancies)} вакансий")


def print_vacancies(vacancies):
    """Выводит информацию о вакансиях"""
    for vacancy in vacancies:
        name = vacancy['name']
        employer = vacancy['employer']['name']
        salary = vacancy.get('salary')
        area = vacancy['area']['name']

        salary_str = "Не указана"
        if salary:
            from_salary = f"{salary['from']} {salary['currency']}" if salary['from'] else ""
            to_salary = f"{salary['to']} {salary['currency']}" if salary['to'] else ""
            salary_str = f"{from_salary} – {to_salary}".strip(" – ")

        print(f"Название: {name}")
        print(f"Компания: {employer}")
        print(f"Зарплата: {salary_str}")
        print(f"Город: {area}")
        print("-" * 50)


# === Основная часть программы ===
if __name__ == '__main__':
    file_worker = JSONFileWorker()
    hh_parser = HH(file_worker)

    # Шаг 1: Загрузить вакансии по ключевому слову
    hh_parser.load_vacancies("python")

    # Шаг 2: Прочитать данные из файла
    vacancies = file_worker.read_data()

    # Шаг 3: Вывести все вакансии
    print_vacancies(vacancies)

    # Шаг 4: Фильтрация по городу
    city = input("Введите город для фильтрации (или Enter, чтобы пропустить): ")
    if city:
        filtered = [v for v in vacancies if v['area']['name'].lower() == city.lower()]
        print(f"\nНайдено вакансий в городе '{city}': {len(filtered)}")
        print_vacancies(filtered)

    # Шаг 5: Фильтрация по минимальной зарплате
    min_salary = input("Введите минимальную зарплату (или Enter, чтобы пропустить): ")
    if min_salary.isdigit():
        min_salary = int(min_salary)
        filtered = [
            v for v in vacancies
            if v.get('salary') and v['salary'].get('from') and v['salary']['from'] >= min_salary
        ]
        print(f"\nНайдено вакансий с зарплатой от {min_salary}: {len(filtered)}")
        print_vacancies(filtered)