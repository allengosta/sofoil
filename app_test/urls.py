from django.conf.urls import include, url
from app_test import views
app_name = 'app_test'

urlpatterns = [
    url(r'^$', views.AssetView.as_view(), name='index'),
    url(r'^asset/(?P<pk>[0-9]+)/well/$', views.well_func, name='detail'),
    url(r'^asset/(?P<pk>[0-9]+)/layer/$', views.layer_func, name='detail2'),
    url(r'^intersection/(?P<id>[0-9]+)/$', views.intersection_func, name='detail_inter'),
]