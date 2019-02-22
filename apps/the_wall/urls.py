from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall$', views.my_wall),
    url(r'^post_msg$', views.create_message),
    url(r'^comment/(?P<msg_id>[0-9]+)$', views.post_comment),
    url(r'^destroy/(?P<msg_id>[0-9]+)$', views.delete_post),
]