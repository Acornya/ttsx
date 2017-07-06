#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from hashlib import sha1
from models import *
# Create your views here.


def index(request):
    return HttpResponse('index')

def register(request):
    context = {'title':'注册'}
    return render(request,'userinfo/register.html',context)
def register_handle(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    uemail = dict.get('email')
    s1 = sha1()
    s1.update(upwd)
    upwd_sha = s1.hexdigest()

    it = UserInfo(uname = uname,upwd = upwd_sha,uemail = uemail)
    it.save()

    return HttpResponse('ok')