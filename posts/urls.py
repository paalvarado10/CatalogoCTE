from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^users_list/$', views.users_list, name='users_list'),
    url(r'^usuario_create/$', views.usuario_create, name='usuario_create'),
    url(r'^user_update/(?P<pk>\d+)$', views.user_update, name='user_update'),
    url(r'^user_update_gti/(?P<pk>\d+)$', views.user_updateGTI, name='user_update_gti'),
    url(r'^user_change_password/$', views.user_change_password, name='user_change_password'),
    url(r'^herramienta_create/$', views.herramienta_create, name='herramienta_create'),
    url(r'^herramienta_update/(?P<pk>\d+)$', views.herramienta_update, name='herramienta_update'),
    url(r'^herramienta_update_revision/(?P<pk>\d+)$', views.herramienta_update_revision, name='herramienta_update_revision'),
    url(r'^herramienta_detail/(?P<pk>\d+)/$', views.herramienta_detail, name='herramienta_detail'),
    url(r'^vigia/$', views.herramientas_vigia, name='vigia'),
    url(r'^revisar/(?P<pk>\d+)$', views.herramienta_revisar, name='revisar'),
    url(r'^actividad_revision/(?P<pk>\d+)$', views.actividad_revision, name='actividad_revision'),
    url(r'^publicar/(?P<pk>\d+)$', views.herramienta_publicar, name='publicar'),
    url(r'^borradores/$', views.borradores_list, name='borradores'),
    url(r'^actividad_create/(?P<pk>\d+)$', views.actividad_create, name='actividad_create'),
    url(r'^actividad_detail/(?P<pk>\d+)/$', views.actividad_detail, name='actividad_detail'),
    url(r'^actividad_update/(?P<pk>\d+)$', views.actividad_update, name='actividad_update'),
    url(r'^actividad_update_revision/(?P<pk>\d+)$', views.actividad_update_revision, name='actividad_update_revision'),
]