 
<h3 style="background: linear-gradient(257deg, Gold, green); -webkit-background-clip: text; color: transparent;">
  Проект курсовая "Поиск вакансий hh.ru"
</h3> 

# 🔖 Описание проекта:

Данный проект реализует "ядро" будущего интернет - магазина.


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


# 🔍 Тестирование:
Реализованы тестирующие модули для модулей приложения.

| Основа | Тесты |
|--------|-------|
| None   | None  |
| None   | None  |
| None   | None  |
 

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

Для получения дополнительной информации обратитесь к [документации](README.md)
