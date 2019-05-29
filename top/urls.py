# coding: utf-8

from django.conf.urls import url

urlpatterns = [
    url(r'^json_log$', 'top.views.json_log', name='top_log'),
    url(r'^$', 'top.views.index', name='top_index'),
]
