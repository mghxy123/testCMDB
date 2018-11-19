#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/16

from django.conf.urls import url
from Testing.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^base/$',base),
    url(r'^et/$',testET),
    url(r'^login/$',login),
]