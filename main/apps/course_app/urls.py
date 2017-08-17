from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete),
    url(r'^courses/process/(?P<id>\d+)$', views.process_destroy),
    url(r'^courses/keep_record$', views.keep_record)
]
