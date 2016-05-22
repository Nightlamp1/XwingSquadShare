from django.conf.urls import url, include
from . import views
from django.views.generic import ListView
from squadbuilder.models import Expansions

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^squadbuilder/$', views.squadbuilder, name='squadbuilder'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.loginview, name='login'),
    url(r'^logout', views.logoutview, name='logout'),
]
