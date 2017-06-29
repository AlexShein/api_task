"""
Создал AShein 28/06/2017
Файл содержит две модели, связанные отношением "один ко многим"
"""

from django.db import models


class Partner(models.Model):
    """
    Модель Партнёр содержит поля "название" и "дата создания"
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)


class Transaction(models.Model):
    """
    Модель содержит поля "дата создания",
    "значение" - сумма транзакции
    "партнёр" - внешний ключ для связи сущности с сущностью "Партнёр"
    """
    created = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    partner = models.ForeignKey(Partner)

    class Meta:
        ordering = ('created',)
