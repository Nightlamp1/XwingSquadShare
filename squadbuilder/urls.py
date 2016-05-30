from django.conf.urls import url, include
from . import views
from django.views.generic import ListView
from squadbuilder.models import Expansions

urlpatterns = [
    url(r'^$', views.squadbuilder, name='squadbuilder')
]
