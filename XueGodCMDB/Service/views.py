# from django.shortcuts import render
# from django.views.generic import View
# from django.http import HttpResponse,JsonResponse

##some testing
# class api(View):
#
#     def post(self,request):
#         if request.POST:
#             postData = request.POST
#             return HttpResponse(postData)
#         login_example = {
#             'type':'user_login',
#             'data':{
#                 'username':'hwile',
#                 'password':'123'
#             },
#             'token':''
#         }
#
#     def get(self,request):
#         if request.GET:
#             getData = request.GET['key']
#             return HttpResponse(getData)

##testing2
# class api(View):
#     def __init__(self,**kwargs):
#         View.__init__(self,**kwargs)
#         self.result = {
#             'status':'',
#             'data':{}
#         }
#
#     def post(self,request):
#         if request.POST:
#             postData = request.POST.get('type')
#             if postData == 'user_login':
#                 self.result['status'] = 'success'
#                 self.result['data']['token'] = '2234'
#             else:
#                 self.result['status'] = 'error'
#                 self.result['data']['error'] = 'no method named %s'%postData
#
#             return JsonResponse(self.result)
#
#     def get(self,request):
#         if request.GET:
#             getData = request.GET['key']
#             return HttpResponse(getData)


# from django.shortcuts import render
# from django.views.generic import View
# from django.http import JsonResponse,HttpResponse
#
# import json
# import time
# import datetime
# import hashlib
#
# from Service.models import LoginUser,APIToken,Service
#
# class api(View):
#     """
#     #........
#     """
#     def __init__(self,**kwargs):
#         View.__init__(self,**kwargs)
#         self.result = {
#             "status": "",
#             "data": {}
#         }
#
#
#     def post(self,request):
#         """
#         处理post请求
#         """
#         if request.POST: #判断是post是否有数据
#             postType = request.POST.get("type") #获取接口请求的类型
#             postData = json.loads(request.POST.get("data")) #获取接口请求的数据
#             if postType == "user_login": #如果请求的是登录
#                 if postData:
#                     username = postData.get("username") #获取提交的用户名
#                     password = postData.get("password") #获取提交的密码
#                     try:
#                         loginUser = LoginUser.objects.get(username = username) #尝试查询用户，这里用户名唯一
#                     except: #查询不到，用户不存在
#                         self.result["status"] = "error"
#                         self.result["data"]["error"] = "no user named %s"%username
#                     else: #查询到进行密码比对
#                         db_password = loginUser.password
#                         if password == db_password: #如果比对成功，生成token，下发
#                             #token存入数据库
#                                 #入库之前进行token校验
#                             try:
#                                 db_token = APIToken.objects.get(user_id = loginUser.id) #获取用户是否有token
#                             except:
#                                 # 生成token，token按照 用户名凭借当前时间的字符串进行md5加密 寿命为 3600 秒
#                                 # 生成token
#                                 token = self.makeToken(username)  # 生成token
#                                 #下发token
#                                 t = APIToken()
#                                 t.value = token
#                                 t.time = datetime.datetime.now()
#                                 t.user_id = loginUser.id
#                                 t.save()
#                                 self.result["status"] = "success"
#                                 self.result["data"]["token"] = token
#                             else:
#                                 db_time_tuple = db_token.time.timetuple()
#                                 db_time_stamp  = time.mktime(db_time_tuple) #数据库时间的时间戳
#
#                                 now_time_tupe = datetime.datetime.now().timetuple()
#                                 now_time_stamp = time.mktime(now_time_tupe) #当前时间的时间戳
#                                 #如果token有效就下发
#                                 if 0 < now_time_stamp - db_time_stamp < 3600:
#                                     self.result["status"] = "error"
#                                     self.result["data"]["error"] = "you have token: %s"%db_token.value
#                                 #如果token失效，就再次生成
#                                 else:
#                                     token = self.makeToken(username)  # 生成token
#
#                                     db_token = datetime.datetime.now()
#                                     db_token.value = token
#                                     db_token.save()
#
#                                     self.result["status"] = "success"
#                                     self.result["data"]["token"] = token
#
#                         else: #比对失败，密码不正确
#                             self.result["status"] = "error"
#                             self.result["data"]["error"] = "%s's error is wrong" % username
#                 else: #值为空
#                     self.result["status"] = "error"
#                     self.result["data"]["error"] = "empty error"
#             else: #请求类型
#                 self.result["status"] = "error"
#                 self.result["data"]["error"] = "no method named %s"%postData
#             return JsonResponse(self.result)
#
#
#     def get(self, request):
#         """
#         处理get请求
#         """
#         if request.GET:
#             getData = request.GET.get("key")
#             return HttpResponse(getData)
#     def makeToken(self,username):
#         """
#             md5算法生成token
#         """
#         time_stamp = str(time.time()) # 获取当前时间的时间的时间戳，然后转换为字符串
#         value = username + time_stamp  # 将值和时间戳字符进行拼接
#
#         md5 =hashlib.md5()
#         md5.update(value.encode())
#         token = md5.hexdigest()
#         return token

from django.shortcuts import render
from django.views.generic import View
from Service.models import *
from django.http import JsonResponse,HttpResponse

import json
import time
import datetime
import hashlib

class api(View):
    """
    #........
    """
    def __init__(self,**kwargs):
        View.__init__(self,**kwargs)
        self.result = {
            "status": "",
            "data": {}
        }


    def post(self,request):
        """
        处理post请求
        """
        if request.POST: #判断是post是否有数据
            postType = request.POST.get("type") #获取接口请求的类型
            postData = json.loads(request.POST.get("data")) #获取接口请求的数据
            if postType == "user_login": #如果请求的是登录
                if postData:
                    username = postData.get("username") #获取提交的用户名
                    password = postData.get("password") #获取提交的密码
                    try:
                        loginUser = LoginUser.objects.get(username = username) #尝试查询用户，这里用户名唯一
                    except: #查询不到，用户不存在
                        self.result["status"] = "error"
                        self.result["data"]["error"] = "no user named %s"%username
                    else: #查询到进行密码比对
                        db_password = loginUser.password
                        if password == db_password: #如果比对成功，生成token，下发
                            #token存入数据库
                                #入库之前进行token校验
                            try:
                                db_token = APIToken.objects.get(user_id = loginUser.id) #获取用户是否有token
                            except:
                                # 生成token，token按照 用户名凭借当前时间的字符串进行md5加密 寿命为 3600 秒
                                # 生成token
                                token = self.makeToken(username)  # 生成token
                                #下发token
                                t = APIToken()
                                t.value = token
                                t.time = datetime.datetime.now()
                                t.user_id = loginUser.id
                                t.save()
                                self.result["status"] = "success"
                                self.result["data"]["token"] = token
                            else:
                                db_time_tuple = db_token.time.timetuple()
                                db_time_stamp  = time.mktime(db_time_tuple) #数据库时间的时间戳

                                now_time_tupe = datetime.datetime.now().timetuple()
                                now_time_stamp = time.mktime(now_time_tupe) #当前时间的时间戳
                                #如果token有效就下发
                                if 0 < now_time_stamp - db_time_stamp < 3600:
                                    self.result["status"] = "error"
                                    self.result["data"]["error"] = "you have token: %s"%db_token.value
                                #如果token失效，就再次生成
                                else:
                                    token = self.makeToken(username)  # 生成token

                                    db_token = datetime.datetime.now()
                                    db_token.value = token
                                    db_token.save()

                                    self.result["status"] = "success"
                                    self.result["data"]["token"] = token

                        else: #比对失败，密码不正确
                            self.result["status"] = "error"
                            self.result["data"]["error"] = "%s's error is wrong" % username
                else: #值为空
                    self.result["status"] = "error"
                    self.result["data"]["error"] = "empty error"
            else: #请求类型
                self.result["status"] = "error"
                self.result["data"]["error"] = "no method named %s"%postData
            return JsonResponse(self.result)


    def get(self, request):
        """
        处理get请求
        """
        if request.GET:
            getData = request.GET.get("key")
            return HttpResponse(getData)
    def makeToken(self,username):
        """
            md5算法生成token
        """
        time_stamp = str(time.time()) # 获取当前时间的时间的时间戳，然后转换为字符串
        value = username + time_stamp  # 将值和时间戳字符进行拼接

        md5 =hashlib.md5()
        md5.update(value.encode())
        token = md5.hexdigest()
        return token