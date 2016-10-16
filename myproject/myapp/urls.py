# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list
from myproject.myapp.views import getfromfile
from myproject.myapp.views import samples

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^getfromfile/$', getfromfile, name='getfromfile'),
    url(r'^samples/$', samples, name='samples'),
]
