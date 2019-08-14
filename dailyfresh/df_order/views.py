from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from df_user.islogin import islogin
from df_user.models import UserInfo
from df_cart.models import CartInfo
from df_order.models import OrderInfo,OrderDetailInfo
from df_goods.models import GoodsInfo
from datetime import datetime
from decimal import Decimal
# Create your views here.


@islogin
def order(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=user_id)
    carts_list = CartInfo.objects.filter(user=user_id)

    get = request.GET
    # 勾选中的商品id
    order_id = get.getlist('order_id')
    print(order_id)
    order_list = []
    for id in order_id:
        order_list.append(CartInfo.objects.get(id=id))
    context = {
        'title': '提交订单',
        'page_name': 1,
        'user': user,
        'carts_list': carts_list,
        'order_list': order_list,
    }
    return render(request,'df_order/place_order.html',context)


def order_handle(request):
    post = request.POST
    # 通过post拿到商品id的列表
    order_id = post.getlist('order_id[]')
    print("order_id",order_id)
    oaddress = post.get('oaddress')
    print("oaddress",oaddress)
    sum_price = post.get('sum_price')
    print("sum_price",sum_price)
    pay_style = post.get('pay_style')
    print(pay_style)
    order_list = []
    for id in order_id:
        order_list.append(CartInfo.objects.get(id=id))

    order = OrderInfo()
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=user_id)
    now = datetime.now()
    order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),user_id)
    order.user_id = user_id
    order.oaddress = oaddress
    order.ototal = Decimal(sum_price[:-1])
    order.odate = now
    order.save()

    for orderid in order_id:
        carts = CartInfo.objects.get(id=orderid)
        good = GoodsInfo.objects.get(pk=carts.goods_id)
        print("good",good.gkucun)
        # 检查库存
        if int(good.gkucun) >= int(carts.count):
            good.gkucun -= int(carts.count)
            good.save()

            goodinfo = GoodsInfo.objects.get(cartinfo__id=orderid)

            # 创建订单详情表
            print("创建订单详情表")
            datailinfo = OrderDetailInfo()
            datailinfo.goods_id = int(goodinfo.id)
            datailinfo.order_id = int(order.oid)
            datailinfo.price = Decimal(int(goodinfo.gprice))
            datailinfo.count = int(carts.count)
            datailinfo.save()
            # 循环删除购物车对象
            carts.delete()
        else:
            return JsonResponse({'ok':1})
    return JsonResponse({'ok':0})




