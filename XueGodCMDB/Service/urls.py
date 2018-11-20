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
]