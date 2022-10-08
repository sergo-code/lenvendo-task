# lenvendo-task

## Скачать chromedriver
Для работы необходимо установить [chromedriver](https://chromedriver.storage.googleapis.com/index.html)
в соответствии с вашей версии Chrome и ОС, и переместить в корень проекта

Настройка pytest.ini
- Windows
```
CHROME=./chromedriver.exe
```
- Linux / MacOS
```
CHROME=./chromedriver
```

## Создать окружение
```
python3 -m venv venv
```

## Установить зависимости
```
python -m pip install -r requirements.txt
```

## Использование
```
pytest -v --setup-show --alluredir=./allure-report
```

Для просмотра отчета необходимо установить 
[Allure Framework](https://docs.qameta.io/allure-report/#_installing_a_commandline)
в соответствии с ващей ОС.