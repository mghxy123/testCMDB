from django.shortcuts import render
from Users.forms import CMDBUserForm

def base(request):
    return render(request,'Testing/blank.html')


def index(request):
    forms= CMDBUserForm
    context = {'forms':forms}
    return render(request,'Testing/index.html',locals())

