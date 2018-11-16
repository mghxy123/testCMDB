from django.shortcuts import render

def base(request):
    return render(request,'Testing/blank.html')