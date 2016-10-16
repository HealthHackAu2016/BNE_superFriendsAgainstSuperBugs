# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list
from myproject.myapp.views import getfromfile

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^getfromfile/$', getfromfile, name='getfromfile')
]
