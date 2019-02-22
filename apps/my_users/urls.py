from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.new_user),
    url(r'^login$', views.user_login),
    url(r'^logout$', views.user_logout),
]