from django.core.paginator import Paginator
from django.shortcuts import render
from .models import GoodsInfo,TypeInfo


# Create your views here.
def index(request):
    # 新品
    fruit = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[:3]
    # 热销商品
    fruit2 = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[:4]
    fish = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[:3]
    fish2 = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[:4]
    meat = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[:3]
    meat2 = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[:4]
    egg = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[:3]
    egg2 = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[:4]
    green = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[:3]
    green2 = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[:4]
    frozen = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[:3]
    frozen2 = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[:4]

    context = {
        'title': '首页',
        'guest_cart': 1,
        'fruit': fruit, 'fruit2': fruit2,
        'fish': fish, 'fish2': fish2,
        'meat': meat, 'meat2': meat2,
        'egg': egg, 'egg2': egg2,
        'green': green, 'green2': green2,
        'frozen': frozen, 'frozen2': frozen2,

    }
    return render(request, 'df_goods/index.html', context)


def goodlist(request,typeid,pageid,sort):
    # typeid为商品类型,pageid为第几页,sort为排序方式
    # 最新发布的商品
    newGoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[:2]
    # 获取商品类型
    goodsType = TypeInfo.objects.get(id=typeid)
    # sort = 2：按价格排序
    if sort == '2':
        order = 'gprice'
    # sort = 3：按人气排序
    elif sort == '3':
        order = '-gclick'
    # sort = 1：按默认排序
    else:
        order = '-id'

    # 全部商品
    allGoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by(order)
    print(allGoods)
    # 分页
    paginator = Paginator(allGoods,15)
    # 根据pageid确定第几页
    pageGoods = paginator.page(int(pageid))
    # 所有页的id
    indexList = paginator.page_range
    context = {
        'title': '商品列表',
        'guest_cart': 1,
        'newGoods':newGoods,
        'pageGoods': pageGoods,
        'typeid':typeid,
        'sort':sort,
        'indexList':indexList,
        'pageid':int(pageid),
        'goodsType':goodsType,

    }
    return render(request, 'df_goods/list.html', context)


def detail(request,id):
    # 当前商品
    good = GoodsInfo.objects.get(id=int(id))
    good.gclick += 1
    good.save()
    # 商品类型
    type_id = good.gtype_id
    try:
        goodsType = TypeInfo.objects.get(id=type_id)
    except:
        print("zhaobudao")
    # 根据当前产品类型获得最新商品
    newGoods = GoodsInfo.objects.filter(gtype_id=type_id).order_by('-id')[:2]
    context = {
        'title': '商品详情',
        'guest_cart': 1,
        'newGoods':newGoods,
        'good':good,
        'goodsType':goodsType,

    }
    response = render(request,'df_goods/detail.html',context)
    # 读取请求的COOKIES
    goods_ids = request.COOKIES.get('goods_ids')
    # 如果拿得到数据,执行下列语句
    if goods_ids and goods_ids != '':
        # 分割成列表
        goods_ids = goods_ids.split(',')
        # 已经存在，就先删掉已经存在的元素
        if id in goods_ids:
            goods_ids.remove(id)
        # 将当前元素插入第一个的位置
        goods_ids.insert(0,id)
        # 只保留前5个
        if len(goods_ids)>5:
            goods_ids = goods_ids[:5]
    # 如果为空
    else:
        goods_ids = id
    # 把列表转换成字符串
    goods_ids = ','.join(goods_ids)
    # 把相应数据放到cookies中
    response.set_cookie('goods_ids',goods_ids)
    return response