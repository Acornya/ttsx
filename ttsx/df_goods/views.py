#coding=utf-8
from django.shortcuts import render
from models import  *
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

def list(request,sort_id):
    onetype = GoodsType.objects.get(pk = int(sort_id))


    context = {'search_flog':'1','title':'列表页','typetitle':onetype.Gsorts}
    return render(request,'goodsinfo/list.html',context)

def detail(request):
    context = {'search_flog':'1','title':'detail页'}
    return render(request,'goodsinfo/detail.html',context)