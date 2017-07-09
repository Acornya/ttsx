from django.conf.urls import  url
import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^list_(\d+)/$', views.list),
    url(r'^detail/$', views.detail),
]