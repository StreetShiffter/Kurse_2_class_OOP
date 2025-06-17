 
<h3 style="background: linear-gradient(257deg, Gold, green); -webkit-background-clip: text; color: transparent;">
  Проект курсовая "Поиск вакансий hh.ru"
</h3> 

# 🔖 Описание проекта:

Данный проект является парсером по сайту HH.ru.


# 🔧 Установка компонентов:


1. Создайте проект и установите poetry:


```pip install --user poetry```

2. Клонируйте репозиторий:


```git clone https://github.com/StreetShiffter/PythonOOPHW.git```

3. Установите инструменты для обработки кода


![Black](https://img.shields.io/badge/black-000000?style=flat&logo=python&logoColor=white)

![Mypy](https://img.shields.io/badge/mypy-checked-blue.svg?logo=python&logoColor=green)

![Flake8](https://img.shields.io/badge/flake8-checked-blue.svg?logo=python&logoColor=blue)

![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=orange)

![Pytest HTML Report](https://img.shields.io/badge/Pytest_HTML_Report-FF6600?style=flat&logo=pytest&logoColor=black)

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?logo=pytest)

![JSON](https://img.shields.io/badge/json-5E5C5C?logo=json&logoColor=red)

# ✒️ Использование
Основное использование приложения запускается из файла *main.py*

# Структура проекта
```
Kurse_2_class_OOP/
├── 📁 data/ # Директория для хранения данных
├── 📁 htmcov/ # Директория для HTML-отчетов
├── 📁 src/ # Основной код приложения
│ ├── 📄init .py # Инициализация пакета
│ ├── 📄class_abstract.py # Абстрактные классы
│ ├── 📄class_api.py # Класс для работы с API
│ ├── 📄class_json_operation.py # Класс для работы с JSON
│ ├── 📄class_vacancy_worker.py # Класс для обработки вакансий
│ └── 📄utils.py # Вспомогательные утилиты
├── 📁 tests/ # Директория для тестов
│ ├── 📄init .py # Инициализация пакета
│ ├── 📄conftest.py # Конфигурация pytest
│ ├── 📄test_class_api.py # Тесты для класса API
│ ├── 📄test_class_json.py # Тесты для класса JSON
│ └── 📄test_class_vacancy_worker.py # Тесты для класса обработки вакансий
├── 📄.coverage # Файл отчета о покрытии тестами
├── 📄.flake8 # Настройки flake8
├── 📄.gitignore # Исключения для Git
├── 📄config.py # Конфигурационный файл
├── 📄main.py # Главный скрипт
├── 📄poetry.lock # Зависимости Poetry
├── 📄pyproject.toml # Конфигурация Poetry
└── 📄README.md # Этот файл
```

# 🔍 Тестирование:
Реализованы тестирующие модули для модулей приложения.

| Основа            | Тесты              |
|-------------------|--------------------|
| class_api         | test_class_api     |
| class_json_worker | test_class_vacancy |
| class_json        | test_class_json    |


*Для проверки тестирования воспользуйтесь командами в терминале:* 

`pytest`
или
`pytest имя_пакета\имя_модуля`

При успешном тестировании будет получены результаты положительного тестирования:
![Положительный результат тестирования](./test_complete.jpg)


pytest --cov # тест покрытия
start htmlcov/index.html  __# запуск отчета в браузере__



***Модуль conftest.py используется для данных тестирования функций.***

*Для полной работы установите фреймворк pytest через poetry*

`poetry add --group dev pytest`

# 📤 Отчет в HTML:

**Для получения отчетов в формате html, воспользуйтесь командами**
```
pytest --cov=src --cov-report=html # формировка отчета для папки src
pytest --cov-report=html # формировка отчета для папки src
pytest --cov # тест покрытия
start htmlcov/index.html  # запуск отчета в браузере

```

Для запуска отчета в браузере:
- на ***Windows***: `start htmlcov/index.html`
- на ***macOS***: `open htmlcov/index.html`
- на ***Linux***: `xdg-open htmlcov/index.html`


# 📝 Документация 

Для получения дополнительной информации обратитесь к [документации](https://api.hh.ru/openapi/redoc#section)
