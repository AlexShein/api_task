"""
Создал AShein 28/06/2017
api_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api_task.views import PartnerViewSet, TransactionViewSet


urlpatterns = [
    url(r'^partner/(?P<pk>[0-9]+)/transaction/?$',
        TransactionViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^partner/(?P<pk>[0-9]+)/?',
        PartnerViewSet.as_view({'get': 'retrieve'})),

    url(r'^admin/', admin.site.urls),
]

