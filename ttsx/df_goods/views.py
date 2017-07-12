#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator
from df_car.models import CarInfo
# Create your views here.
def index(request):
    all_list = []
    type_list = GoodsType.objects.all()
    for type_cell in type_list:
        glist = type_cell.goodsinfo_set.order_by('-id')[0:4]
        clist = type_cell.goodsinfo_set.order_by('-gclick')[0:4]
        all_list.append({'t1':type_cell,'glist':glist,'clist':clist})
    context = {'all_list':all_list,'title':'首页','search_flog':'1'}

    return render(request, 'goodsinfo/index.html',context)

def list(request,sort_id,recv_index):

    onetype = GoodsType.objects.get(pk=int(sort_id))
    newgoods = onetype.goodsinfo_set.order_by('-id')[0:2]
    idgoods = onetype.goodsinfo_set.order_by('-id')

    p = Paginator(idgoods,1)
    recv_ix = int(recv_index)
    if recv_ix<1:
        recv_ix = 1
    elif recv_ix > p.num_pages:
        recv_ix = p.num_pages

    plist = p.page(recv_ix)   #第一页的数据


    context = {'search_flog':'1','title':'列表页','typetitle':onetype.Gsorts,'newgoods':newgoods,'idgoods':idgoods,
               'plist':plist,'onetype':onetype,}
    return render(request,'goodsinfo/list.html',context)

def detail(request,pic_id):
    pic_i = int(pic_id)

    it = GoodsInfo.objects.get(pk = pic_i)
    it.gclick += 1
    it.save()

    sort_id = it.grelation.id
    onetype = GoodsType.objects.get(pk=int(sort_id))
    newgoods = onetype.goodsinfo_set.order_by('-id')[0:2]
    context = {'search_flog':'1','title':'detail页','newgoods':newgoods,'it':it}
    fanhui = render(request, 'goodsinfo/detail.html', context)
    goods_str = request.COOKIES.get('goods_history','')
    if goods_str == '':
        goods_str = pic_id

    else:

        goods_str =   pic_id + ',' + goods_str
        goods_list = goods_str.split(',')
        if len(goods_list) > 5:
            goods_list.pop()
            goods_str = ','.join(goods_list)


    fanhui.set_cookie('goods_history',goods_str,max_age=60*60*24*5)
    return fanhui

def islogin(request):
    if request.session.get('uid'):
        context = {'flog':1}

    else:
        context = {'flog':0}

    return JsonResponse(context)

def cart_save(request):
    r=request.GET
    good_id = int(r.get('good_id'))
    user_id = request.session.get('uid')
    #if goods in cart
    list_goods = CarInfo.objects.filter(cgoods_id = good_id, cuser_id = user_id)

    if len(list_goods) == 1:

        list_goods[0].count += 1

        list_goods[0].save()
        return JsonResponse({'flog': 1})
    else:
        try:
            car = CarInfo(cgoods_id = good_id, cuser_id = user_id, count = 1)
            car.save()
            return JsonResponse({'flog':1})
        except:
            return JsonResponse({'flog':0})


def cart_save_detail(request):
    r = request.GET
    good_id = int(r.get('good_id'))
    good_num = int(r.get('good_num'))
    user_id = request.session.get('uid')
    # if goods in cart
    list_goods = CarInfo.objects.filter(cgoods_id=good_id, cuser_id=user_id)

    if len(list_goods) == 1:

        list_goods[0].count += good_num

        list_goods[0].save()
        return JsonResponse({'flog': 1})
    else:
        try:
            car = CarInfo(cgoods_id=good_id, cuser_id=user_id, count=good_num)
            car.save()
            return JsonResponse({'flog': 1})
        except:
            return JsonResponse({'flog': 0})

def show_count(request):
    user_id = request.session.get('uid')
    typenum = CarInfo.objects.filter(cuser_id=user_id).count()

    context = {'typenum':typenum}
    return JsonResponse(context)

