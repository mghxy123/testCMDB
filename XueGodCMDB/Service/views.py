from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse

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

class api(View):
    def __init__(self,**kwargs):
        View.__init__(self,**kwargs)
        self.result = {
            'status':'',
            'data':{}
        }

    def post(self,request):
        if request.POST:
            postData = request.POST.get('type')
            if postData == 'user_login':
                self.result['status'] = 'success'
                self.result['data']['token'] = '2234'
            else:
                self.result['status'] = 'error'
                self.result['data']['error'] = 'no method named %s'%postData

            return JsonResponse(self.result)

    def get(self,request):
        if request.GET:
            getData = request.GET['key']
            return HttpResponse(getData)


