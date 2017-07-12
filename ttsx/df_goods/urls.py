from django.conf.urls import  url
import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^list_(\d+)_(\d+)/$', views.list),
    url(r'^(\d+)/$', views.detail),
    url(r'^islogin/$', views.islogin),
    url(r'^cart_save/$', views.cart_save),
    url(r'^cart_save_detail/$', views.cart_save_detail),
    url(r'^show_count/$', views.show_count),

]
