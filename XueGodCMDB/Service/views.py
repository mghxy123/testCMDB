from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse

class api(View):

    def post(self,request):
        if request.POST:
            postData = request.POST
            return HttpResponse(postData)
        login_example = {
            'type':'user_login',
            'data':{
                'username':'hwile',
                'password':'123'
            },
            'token':''
        }

    def get(self,request):
        if request.GET:
            getData = request.GET['key']
            return HttpResponse(getData)
