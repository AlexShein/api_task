"""
Создал AShein 28/06/2017
Файл содержит две модели, связанные отношением "один ко многим"
"""

from django.db import models


class Partner(models.Model):
    """
    Модель Партнёр, отображает доверенного партнёра компании
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)


class Transaction(models.Model):
    """
    Модель отражает изменения состояния счёта партнёра
    """
    created = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    partner = models.ForeignKey(Partner)

    class Meta:
        ordering = ('created',)
