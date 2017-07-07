from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^uname_confm/$', views.uname_confm),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^login_handle/$', views.login_handle),
    url(r'^center/$', views.center),
    url(r'^books/$', views.books),
    url(r'^shouaddr/$', views.shouaddr),
    url(r'^addr_handle/$', views.addr_handle),
    url(r'^close/$', views.close),
]