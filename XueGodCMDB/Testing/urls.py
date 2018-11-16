#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/16

from django.conf.urls import include, url
from Testing.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$',index),
    url(r'^base/$',base),
]