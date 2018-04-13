from django.conf.urls import url, include
from . import views, models

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^addUsuario/$', views.addUsuario, name='addUsuario'),
    url(r'^user_update/(?P<pk>\d+)$', views.user_update, name='user_update'),
    url(r'^user_change_password/$', views.user_change_password, name='user_change_password')
]