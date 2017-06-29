# api_task
Simple Django REST Framework API
Разработал А. Шеин 28-29.06.17

Использование:
* Запустите Django server by "./mange.py runserver"
* Откройте http://127.0.0.1:8000/admin/ и создайте пару записей партнёров
* Используйте curl и запросы следущего вида для добавления записей транзакций:
"curl -X POST -d value=-130.0 -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/partner/2/transaction/",
где в /pratner/<PK>/transaction <PK> замените на id созданного партнёра. Дата транзакции проставится автоматически.
* Для отображения истории транзакций партнёра используйте curl и запрос следующего вида:
"curl -G  -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/partner/1/transaction/",
где в /pratner/<PK>/transaction <PK> замените на id созданного партнёра.
* Для отображения баланса партнёра на конкретную дату используйте 
"curl -G -d date=2017-06-29 -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/partner/1/",
"-d date=....-..-.." - необязательный параметр, без него по умолчанию баланс будет отображаться на текущий день.

