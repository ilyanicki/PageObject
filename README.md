Это учебный проект по автомазиции тестирования с применением паттерна Page Object Model

Для запуска тестов и генерации отчёта выполнить команду 
rm -rf allure-results/
pytest -v --alluredir=allure-results 
allure serve allure-results
