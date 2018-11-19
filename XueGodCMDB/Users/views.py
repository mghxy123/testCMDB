from django.http import JsonResponse,HttpResponse
# Create your views here.

def register(request):
    # if request.method == 'POST':
    #     return JsonResponse({"method":'POST'})
    #
    # else:
    #     return JsonResponse({"method":"GET"})

    result = {"submit":'success'}
    #判断三个，请求的方法，post请求的内容和，请求的文件
    #判断请求方式是否为post，request.POST的意思是判断请求是否有数据，request。files是判断上传是否有文件
    if  request.method =='POST' and request.POST and request.FILES:
        register_data = CMDBUserForm(data=request.POST,files=request.FILES)
        if register_data.is_valid():
            #检验成功
            register_post_data = register_data.cleaned_data

            username = register_post_data.get('username')
            password = register_post_data.get('password')
            nickname = register_post_data.get('nickname')
            phone = register_post_data.get('phone')
            email = register_post_data.get('email')

            #当去get图片的时候的导师是一个对象，用。name是获取photo的值
            photo = register_post_data.get('photo').name

            CMDBUser.objects.create(
                username= username,
                password= password,
                nickname=nickname,
                phone=phone,
                email=email,
                photo=photo,

            )
            photofile = request.FILES.get('photo')
            photoSavePath=os.path.join(BASE_DIR,'media/images/%s'%photofile.name)
            with open(photoSavePath,'wb') as pf:
                for chunk in photofile.chunks():
                    pf.write(chunk)
            return JsonResponse(result)
        else:
            result["submit"] = "failed"
            print(register_data.errors)
            return JsonResponse(result)
    else:
        return JsonResponse({"method":'GET'})


import os
from django.shortcuts import render
from Users.forms import CMDBUserForm
from Service.models import CMDBUser
from XueGodCMDB.settings import BASE_DIR
from django.shortcuts import render_to_response

def loginValid(func):
    def valid(request,*args,**keywords):
        username = request.COOKIES.get("username")
        if username:
            try:
                user = CMDBUser.objects.get(username = username)
            except:
                return HttpResponseRedirect("/testing/login/", locals())
            else:
                return func(request)
        else:
            return HttpResponseRedirect("/testing/login/",locals())
    return valid

@loginValid
def index(request):
    forms = CMDBUserForm() #定义form表单
    if request.method == "POST" and request.POST and request.FILES:
        #判断
            #1、请求方式是post
            #2、post请求有内容
            #3、文件请求有内容
        formsData = CMDBUserForm(data = request.POST,files = request.FILES)
        #校验提交的数据和文件
        if formsData.is_valid():
            requestData = formsData.cleaned_data
            username = requestData.get("username")
            password = requestData.get("password")
            nickname = requestData.get("nickname")
            phone = requestData.get("phone")
            email = requestData.get("email")
            photo = requestData.get("photo").name #这里获取到的不是一个值，而是一个文件对象

            user = CMDBUser() #实例化数据库，保存数据
            user.username = username
            user.password = password
            user.nickname = nickname
            user.phone = phone
            user.email = email
            user.photo = photo
            user.save()

            #保存文件，这里没有限制文件格式，上传啥都行
            photofile = request.FILES.get("photo")
            path = os.path.join(BASE_DIR,"media/images/%s"%photofile.name)
            with open(path,"wb") as f:
                for chunk in photofile.chunks():
                    f.write(chunk)
        else:
            print(formsData.errors)
    return render(request,"testing/",locals())

# def echartExample(request):
#     return render(request,"echartsExample.html")

from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
def login(request):
    if request.method == "POST" and request.POST:
        #获取校验cookie
        login_cookie = request.get_signed_cookie(key = "login_cookie",salt = "nihao")
        if login_cookie:
            data = request.POST
            username = data.get("username")
            password = data.get("password")
            try:
                user = CMDBUser.objects.get(username = username)
            except:
                return HttpResponse("用户不存在")
            else:
                db_password = user.password
                if password == db_password:
                    response = HttpResponseRedirect("testing/index/",locals())
                    response.set_cookie(key = "username",value = user.username)
                    return response
                else:
                    return HttpResponse("密码错误")

        else:
            return HttpResponse("404")
    else:
        #登陆页面，login.html get请求
        #生成response实例
        response = render(request,"testing/login/")
        #设置cookie
        response.set_signed_cookie("login_cookie","while",salt = "nihao",max_age = 3600)
        #返回设置了cookie的响应
        return response
