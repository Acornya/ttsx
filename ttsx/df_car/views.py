#coding=utf-8
from django.shortcuts import render
from models import *
from df_goods.models import GoodsInfo
from django.http import JsonResponse
# Create your views here.

def car(request):
    uid = request.session.get('uid')
    ugoodslist = CarInfo.objects.filter(cuser_id=uid)
    total = ugoodslist.count()
    goodsobj = []
    for one in ugoodslist:
        obj = GoodsInfo.objects.get(id=one.cgoods_id)
        count = one.count
        goodsobj.append({'obj':obj,'count':count})
    context = {'title':'购物车','goodsobj':goodsobj,'total':total}
    return render(request,'car/cart.html',context)

def dele(request):
    r = request.GET
    del_id = int(r.get('del_id'))
    uid = request.session.get('uid')
    ugoodslist = CarInfo.objects.filter(cuser_id=uid).exclude(cgoods_id=del_id)
    ugoodslist[0].delete()
    return JsonResponse({"flag":1})