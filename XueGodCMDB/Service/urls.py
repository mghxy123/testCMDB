#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/16

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import View
from Service.views import *

urlpatterns = [
    url(r'^api/',api.as_view()),
]