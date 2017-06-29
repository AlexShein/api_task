"""
Создал AShein 28/06/2017
В данном файле содержится код сериализаторов PartnerSerializer,
TransactionSerializer
"""

from datetime import datetime, timezone
from django.db.models import Sum, Q
from rest_framework import serializers
from api_task.models import Partner, Transaction


class PartnerSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField('count_balance')

    def count_balance(self, obj):
        """
        Функция для расчёта баланса партнёра.
        Для возможности расчёта на конкретный момент времени
        получаем парамет date из request.query_params
        """

        request = self.context.get('request')
        if request and 'date' in request.query_params:
            date = self.context['request'].query_params['date']
        else:
            date = datetime.now(timezone.utc)
        balance = Transaction.objects.filter(Q(partner_id=obj.id) &
                                             Q(created__lt=date)).aggregate(Sum('value'))
# Проверка для удобства отображения - 0 вместо null, если транзакций не было.
        if balance['value__sum'] is None:
            balance['value__sum'] = 0
        return balance

    class Meta:
        model = Partner
        fields = ['id', 'name', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    partner = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        """
        Создание `Transaction`, заполнение validated набором данных.
        """

        partner_id = self.context['view'].kwargs['pk']
        return Transaction.objects.create(partner_id=partner_id, **validated_data)

    class Meta:
        model = Transaction
        fields = ['id', 'partner', 'value', 'created']
