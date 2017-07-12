#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
from models import *
import datetime
from auth_decoration import *
from df_goods.models import GoodsInfo
# Create your views here.


def index(request):
    return HttpResponse('index')


def register(request):
    context = {'title':'注册','hair_flog':'0'}
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

    return redirect('/usr/login/')


def uname_confm(request):
    r = request.GET
    newname = r.get('uname')
    it = UserInfo.objects.filter(uname = newname)
    if len(it)==1:
        context = {'flog':'1'}
        return JsonResponse(context)
    else:
        return JsonResponse({'flog':'0'})


def login(request):
    context = {}
    context['title'] = '登录'
    context['hair_flog'] = '0'
    if request.COOKIES.get('uname') == None:
        context['rem_name'] = ''
    else:
        context['rem_name']=request.COOKIES.get('uname')
    # print request.COOKIES.get('uname')

    return render(request,'userinfo/login.html',context)


def login_handle(request):
    dict = request.POST
    uname = dict.get('username')
    upwd = dict.get('pwd')
    remember = dict.get('remember')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha = s1.hexdigest()
    context = {'pwd_flog':'0'}
    it = UserInfo.objects.get(uname = uname)
    if it.upwd == upwd_sha:
        request.session['uid'] = it.id
        request.session['uname'] = it.uname
        fanhui = redirect(request.session.get('lastpath', '/'))
        if remember == 'on':
            # print 'on'
            fanhui.set_cookie('uname',value=uname,expires= datetime.date.today()+ datetime.timedelta(1))
        return fanhui
    else:
        context['title'] = '重新登录'
        context['pwd_flog'] = '1'
        context['uname'] = uname
        return render(request,'userinfo/login.html',context)


@auth
def center(request):
    context = {'title':'用户中心'}
    list = UserInfo.objects.filter(pk = request.session.get('uid'))
    if len(list) == 1:
        uname = list[0].uname
        uphone = list[0].uphone
        ucode = list[0].ucode
        uaddr_detail = list[0].uaddr_detail
        uemail = list[0].uemail
        context['uname'] = uname
        context['uphone'] = uphone
        context['ucode'] = ucode
        context['uaddr_detail'] = uaddr_detail
        context['uemail'] = uemail
        good_str = request.COOKIES.get('goods_history','')
        if good_str == '':
            pass
        else:
            good_list = good_str.split(',')
            ob_list = []
            for good in good_list:
                egg = GoodsInfo.objects.get(pk = int(good))
                ob_list.append(egg)
            context['ob_list'] = ob_list
        return render(request, 'userinfo/center.html', context)
    else:
        return redirect('/usr/login/')


@auth
def books(request):
    context = {'title': '订单'}
    r = UserInfo.objects.filter(pk=request.session.get('uid'))
    context['uname'] = r[0].uname
    return render(request, 'userinfo/books.html', context)

@auth
def shouaddr(request):
    context = {'title': '收获地址'}
    r = UserInfo.objects.filter(pk = request.session.get('uid'))
    context['addr_detail'] = r[0].uaddr_detail
    context['urcv'] = r[0].uname
    context['uphone'] = r[0].uphone
    context['uname'] = r[0].uname

    return render(request, 'userinfo/shouaddr.html', context)


def addr_handle(request):
    r = request.POST
    recv_name = r.get('recv_name')
    addr_detail = r.get('addr_detail')
    ucode = r.get('ucode')
    uphone = r.get('phone')
    p = UserInfo(urcv=recv_name, uaddr_detail=addr_detail, ucode=ucode, uphone=uphone)
    p.save()
    context = {'addr_detail':addr_detail,'urcv':recv_name,'uphone':uphone}
    context['title'] = '地址'
    return render(request,'userinfo/shouaddr.html',context)


def close(request):
    print('noonooonoononoo')
    request.session.flush()
    return JsonResponse()

def logout(request):
    request.session.flush()
    return redirect('/usr/login/')





