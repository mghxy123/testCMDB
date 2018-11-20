from django.shortcuts import render,HttpResponseRedirect
from Users.forms import CMDBUserForm
from django.http import HttpResponse,JsonResponse
from Service.models import CMDBUser

def base(request):
    return render(request,'testing/blank.html')


def index(request):
    forms= CMDBUserForm
    context = {'forms':forms}
    return render(request,'testing/index.html',locals())

def testET(request):
    return render(request,'testing/testET.html')

##简单的检验cookie
# def login(request):
#     #生成response实例
#     response = render(request,'testing/login.html')
#     #设置cookie，和过期时间
#     # response.set_cookie('loginCookie','thisTestCookie',max_age=360)
#     #加盐cookie
#     response.set_signed_cookie('loginCookie','thisTestCookie',salt = "good",max_age=360)
#     #设置返回cookie的响应
#     return response


#校验cookie和cookie的使用
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
                    response = HttpResponseRedirect("/index/",locals())
                    response.set_cookie(key = "username",value = user.username)
                    return response
                else:
                    return HttpResponse("密码错误")

        else:
            return HttpResponse("404")
    else:
        #登陆页面，login.html get请求
        #生成response实例
        response = render(request,"testing/login.html")
        #设置cookie
        response.set_signed_cookie("login_cookie","while",salt = "nihao",max_age = 3600)
        #返回设置了cookie的响应
        return response
