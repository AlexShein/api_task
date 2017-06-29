"""
Создал AShein 28/06/2017
Для удобства тестирования(добавления записей) добавляю в админ меню
модели Partner и Transaction
"""


from django.contrib import admin
from api_task.models import Partner, Transaction


class PartnerAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Transaction, TransactionAdmin)
