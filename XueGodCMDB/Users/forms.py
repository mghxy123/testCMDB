#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : forms.py
# Author: HuXianyong
# Date  : 18/11/16

from django import forms

class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length=32, label="用户账号",widget = forms.TextInput(
        attrs = {
            "class":"form-control",
            "required":"True",
            "minlength": 2,
            "maxlength": 6
        }))
    password = forms.CharField(max_length=32,label="用户密码",widget= forms.PasswordInput(
        attrs = {
            "class":"form-control",
            "required": "True",
            "minlength": 2,
            "maxlength": 6
        }))
    nickname = forms.CharField(max_length=32, label="用户姓名",widget = forms.TextInput(
        attrs = {
            "class":"form-control",
            "required": "True",
            "minlength": 2,
            "maxlength": 6
    }))
    phone = forms.CharField(max_length=32, label="用户电话",widget = forms.TextInput(
        attrs = {
            "class":"form-control",
            "required": "True"
    }))
    email = forms.EmailField(label="用户邮箱",widget = forms.EmailInput(
        attrs = {
            "class":"form-control",
            "requeired": True,
        }))
    photo = forms.ImageField(label="用户头像")
