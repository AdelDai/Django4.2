```
Иструкция
```
В любом терминале прописываем:
python3 -m venv venv
# После этого ее нужно активировать:
source venv/bin/activate (это нужно для Linux)

venv\Scripts\activate (для Windows)
# Приступаем к скачивание всех необходимых библиотек (зависимости)
pip install -r requirements.txt
# Все готово теперь запускаем все в dev-режиме
cd lyceum
python manage.py runserver
