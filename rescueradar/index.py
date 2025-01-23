from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
    return render(request,'faild.html')