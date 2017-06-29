"""
Создал AShein 28/06/2017
ViewSets для отображения данных партнёров и транзакций
"""

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView
from api_task.serializers import PartnerSerializer, TransactionSerializer
from api_task.models import Partner, Transaction


class PartnerViewSet(RetrieveAPIView):
    """
    API endpoint для просмотра баланса партнёров.
    """
    queryset = Partner.objects.all().order_by('created')
    serializer_class = PartnerSerializer


class TransactionViewSet(
        viewsets.GenericViewSet,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.ListModelMixin):
    """
    API endpoint для просмотра и добавления транзакций партнёров.
    """
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        Должны отображаться все транзакции выбранного пользователя
        """
        return Transaction.objects.filter(partner_id=self.kwargs['pk'])
