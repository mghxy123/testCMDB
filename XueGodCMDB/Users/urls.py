#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/16

from django.conf.urls import  url
from Users.views import *


urlpatterns = [
    url(r'^register/',register),
]
