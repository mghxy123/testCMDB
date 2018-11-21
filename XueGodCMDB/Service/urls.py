#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/16

from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from Service.views import *

urlpatterns = [
    url(r'^api/',csrf_exempt(api.as_view())),
    url(r'^serverData/',csrf_exempt(api.as_view())),
    url(r'^serverList/', serverList),  # as_view让我们定义的视图类像函数一样被调用
    url(r'^serverData/', serverData),  # as_view让我们定义的视图类像函数一样被调用
]