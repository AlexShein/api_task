"""
Создал AShein 28/06/2017
api_task URL Configuration

"""
from django.conf.urls import url
from django.contrib import admin
from api_task.views import PartnerViewSet, TransactionViewSet


urlpatterns = [
    url(r'^partner/(?P<pk>[0-9]+)/transaction/?$',
        TransactionViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^partner/(?P<pk>[0-9]+)/?',
        PartnerViewSet.as_view()),

    url(r'^admin/', admin.site.urls),
]
