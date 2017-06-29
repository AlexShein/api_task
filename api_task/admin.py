"""
Создал AShein 28/06/2017
Для удобства тестирования(добавления записей) добавляю в админ меню
модели Partner и Transaction
"""


from django.contrib import admin
from api_task.models import Partner, Transaction


admin.site.register([Partner, Transaction])
