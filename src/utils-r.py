from src.class_vacancy_worker import Vacancy
from src.class_api import HeadHunterAPI
from src.class_json import JSONSaver


def user_interaction():
    # Шаг 1: Выбор платформы
    platforms = ["HeadHunter"]
    print("Доступные платформы для поиска вакансий:")
    for i, platform in enumerate(platforms, start=1):
        print(f"{i}. {platform}")

    choice = int(input("Выберите платформу (введите номер): "))
    if choice != 1:
        print("Неподдерживаемая платформа.")
        return

    # Шаг 2: Поисковой запрос
    search_query = input("Введите поисковый запрос (например, 'Python developer'): ")

    # Получение вакансий через API
    hh_api = HeadHunterAPI()
    try:
        vacancies_data = hh_api.get_vacancies(search_query)
    except Exception as e:
        print(f"Ошибка получения данных: {e}")
        return

    # Преобразование в объекты Vacancy
    vacancies_list = Vacancy.cast_to_object_list(vacancies_data)

    # Шаг 3: Количество топ-вакансий
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print("Некорректный ввод, устанавливается значение по умолчанию — 5")
        top_n = 5

    # Шаг 4: Фильтрация по ключевым словам
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").lower().split()
    if filter_words:
        filtered_vacancies = [
            v for v in vacancies_list
            if any(word in v.name.lower() or (v.description and word in v.description.lower())
                   for word in filter_words)
        ]
    else:
        filtered_vacancies = vacancies_list

    # Шаг 5: Фильтрация по зарплате
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")
    if salary_range:
        try:
            salary_min, salary_max = map(int, salary_range.replace(" ", "").split("-"))
            ranged_vacancies = [
                v for v in filtered_vacancies
                if (v.salary_from or 0) >= salary_min and (v.salary_to or float('inf')) <= salary_max
            ]
        except ValueError:
            print("Некорректный формат диапазона зарплат. Пример: 100000-150000")
            ranged_vacancies = filtered_vacancies
    else:
        ranged_vacancies = filtered_vacancies

    # Шаг 6: Сортировка по зарплате
    sorted_vacancies = Vacancy.sort_vacancies_by_salary(ranged_vacancies, reverse=True)

    # Шаг 7: Вывод топ-N вакансий
    top_vacancies = sorted_vacancies[:top_n]

    if not top_vacancies:
        print("По вашему запросу не найдено подходящих вакансий.")
        return

    print("\nТоп вакансий по вашему запросу:")
    for i, vacancy in enumerate(top_vacancies, 1):
        print(f"{i}. {vacancy.name} ({vacancy.area})")
        print(f"   Зарплата: {vacancy.salary_from} - {vacancy.salary_to}")
        print(f"   Описание: {vacancy.description}")
        print(f"   Ссылка: {vacancy.link}")
        print()

    # Шаг 8: Сохранение в файл
    save_choice = input("Сохранить эти вакансии в файл? (да/нет): ").strip().lower()
    if save_choice == "да":
        saver = JSONSaver()
        for vacancy in top_vacancies:
            saver.add_vacancy(vacancy)
        print("Вакансии сохранены.")

    # Шаг 9: Удаление вакансии по желанию
    delete_choice = input("Хотите удалить какую-то вакансию из списка? (да/нет): ").strip().lower()
    if delete_choice == "да":
        try:
            index = int(input("Введите номер вакансии для удаления: ")) - 1
            if 0 <= index < len(top_vacancies):
                selected_vacancy = top_vacancies[index]
                saver.delete_vacancy(selected_vacancy)
                print("Вакансия удалена.")
            else:
                print("Неверный номер.")
        except ValueError:
            print("Некорректный ввод номера вакансии.")
