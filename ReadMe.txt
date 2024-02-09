#-----------------------------#
 Используется Python 3.12
#-----------------------------#


Разрешения на компьютере для запуска виртуального окружения:
-Разрешить скрипты для окружения
 Set-ExecutionPolicy AllSigned
-Запретить скрипты для окружения
 Set-ExecutionPolicy Restricted
-Проверка разрешения
 Get-ExecutionPolicy


Установка виртуального окружения
 py -3 -m venv venv
Запуск виртуального окружения если не установилось по умолчанию
 venv/Scripts/activate


Установка необходимых компонентов для автотестов с нуля:
 pip install selenium
 pip install webdriver-manager
 pip install pytest-html
 pip install pydantic
 pip freeze > requirements.txt

Установка необходимых компонентов для автотестов из файла:
 pip install -r requirements.txt

Перед запуском тестов необходимо проверить файл: 'Config.py'

Запуск тестов
 pytest
Запуск тестов с комментариями
 pytest -v -s
Запуск тестов с условием 
 pytest -v -s -m "not smoke"
Запуск тестов с отчетом
 pytest --html=Report/index.html --self-contained-html  (Без -s -v!)
Запуск конкретного теста с отчетом 
 pytest --html=Report/index.html --self-contained-html Tests/Interface/test_main_page_not_authorized.py::TestMainPage::test_check_header_button

