from django.conf.urls import url, include
from . import views, models

urlpatterns = [
    url(r'^$', views.index, name='index'),
]