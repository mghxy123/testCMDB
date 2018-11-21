#!/usr/bin/python
# -*- coding: utf8 -*- 
#*************************************************************************
# File Name: requests_sendData5.py
# Author: huxianyong
# Mail: hxy123@163.com 
# Created Time: Wed 21 Nov 2018 01:49:50 PM CST
#************************************************************************


import json
import requests

url = "http://47.98.60.53:9909/service/api/"
#对嵌套部分进行json封装
#login_data = json.dumps({
#    "username": "while",
#    "password": "123"
#})
login_data = json.dumps({
    "ip": "192.168.1.88",
    "mac": "00:01:6C:06:A6:29",
    "cpu": "Intel(R) Core(TM) i7 CPU L 640  @ 2.13GHz",
    "memory": "180004",
    "hostname": "saltmaster"
})

data = {
   "type": "addServer",
    "data": login_data,
    "token": "5520a720a713954c2fa63f22996fdfcc"
}

response = requests.post(url,data = data)
data = response.json()
print(data)
