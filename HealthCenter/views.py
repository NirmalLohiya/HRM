from django.shortcuts import render
from HealthCenter.models import *
from django.http import HttpResponse
# Create your views here.


def view_home(request):
    resp=render(request , 'HealthCenter/home.html')
    return resp

def view_register(request):
    if request.method=='GET':
        resp=render(request, 'HealthCenter/register.html')
        return resp
    elif request.method=='POST':
        r=Register()
        r.firstname=request.POST.get("firstname",0)
        r.lastname=request.POST.get("lastname",0)
        r.email=request.POST.get("email",0)
        r.password=request.POST.get("password",0)
        r.save()
        return HttpResponse('<p>data is added</p>')
    else:
        return HttpResponse('<p>not the a valid data</p>')


def view_login(request):
    if request.method=='GET':
        resp=render(request, 'HealthCenter/login.html')
        return resp
    elif request.method=='POST':
        l=Login()
        l.email=request.POST.get("lemail",0)
        l.password=request.POST.get("lpassword",0)
        l.save()
        return HttpResponse('<p>data is added</p>')
    else:
        return HttpResponse('<p>not the valid data</p>')


def view_secure(request):
    resp=render(request, 'HealthCenter/secure.html')
    return resp


def view_unsecure(request):
    resp=render(request, 'HealthCenter/unsecure.html')
    return resp