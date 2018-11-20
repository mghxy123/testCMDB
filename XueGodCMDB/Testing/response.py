#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : response.py
# Author: HuXianyong
# Date  : 2018/11/20

import os
import uuid
import socket


class GetData():
    def __init__(self):
        self.result = {}

    def getResult(self,fun):
        def inner():
            key,value = fun(self)
            self.result[key] = value
        return inner

    def getData_byFile(self,command,keyword):
        result = ''
        with os.popen(command) as f :
            for line in f.readlines():
                key,value = line.split(':')
                key = key.strip()
                value = value.strip()
                if key == keyword:
                    result = value
                    break
        return result
    @getResult
    def get_cpu(self):
        command = 'cat /proc/cpuinfo|grep -v "^$"'
        keyword = 'model name'
        cpuData = self.getData_byFile(command,keyword)
        return 'cpuData',cpuData

    @getResult
    def get_mem(self):
        command = 'cat /proc/meminfo|grep -v "^$"'
        keyword = 'MemTotal'
        meminfo = self.getData_byFile(command,keyword)
        return 'meminfo',meminfo

    @getResult
    def get_hostname(self):
        self.hostname = socket.gethostname()
        return 'hostname',self.hostname

    @getResult
    def get_ip(self):
        ip = socket.gethostbyname(self.hostname)
        return 'ip',ip

    @getResult
    def get_mac(self):
        mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
        mac = ':'.join(mac[i:i+2] for i in range(0,11,2))
        return 'mac',mac


if __name__ == '__main__':
    data = GetData()
    data.get_cpu()

    print(data.result)