#coding=utf-8
from django.shortcuts import render
from models import  *
from django.core.paginator import Paginator
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
    onetype = GoodsType.objects.get(pk = int(sort_id))
    newgoods = onetype.goodsinfo_set.order_by('-id')[0:2]
    idgoods = onetype.goodsinfo_set.order_by('id')
    p = Paginator(idgoods,1)
    recv_ix = int(recv_index)
    print(recv_ix)
    if recv_ix<1:
        recv_ix = 1
    elif recv_ix > p.num_pages:
        recv_ix = p.num_pages

    plist = p.page(recv_ix)   #第一页的数据


    context = {'search_flog':'1','title':'列表页','typetitle':onetype.Gsorts,'newgoods':newgoods,'idgoods':idgoods,
               'plist':plist,'onetype':onetype,}
    return render(request,'goodsinfo/list.html',context)

def detail(request,pic_id):
    r = request.GET
    
    print(r.get('psort'))



    pic_i = int(pic_id)
    it = GoodsInfo.objects.get(pk = pic_i)
    sort_id = it.grelation.id
    onetype = GoodsType.objects.get(pk=int(sort_id))
    newgoods = onetype.goodsinfo_set.order_by('-id')[0:2]
    context = {'search_flog':'1','title':'detail页','newgoods':newgoods,'it':it}
    return render(request,'goodsinfo/detail.html',context)