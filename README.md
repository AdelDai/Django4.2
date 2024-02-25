```
Иструкция
```
***В любом терминале прописываем:***
***python3 -m venv venv***
```
После этого ее нужно активировать:
```
***source venv/bin/activate (это нужно для Linux)***

***venv\Scripts\activate (для Windows)***
```
Приступаем к скачивание всех необходимых библиотек (зависимости)
```
## Чтобы запустить проект прописываем:
***pip install -r  requirements\prod.txt***
## Чтобы протестировать проект прописываем:
***pip install -r  requirements\dev.txt***
## Для разроботки проекта прописываем:
***pip install -r  requirements\test.txt***
```
чтобы запустить сервер в dev-режиме:
```
***cd lyceum***

***python manage.py runserver***
