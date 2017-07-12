from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.car),
    url(r'^dele/$', views.dele),
]