from django.shortcuts import render
from .models import CartInfo
from django.http.response import JsonResponse
from df_user.islogin import *
# Create your views here.
@islogin
def cart(request):
    # 获取当前用户id
    user_id = request.session.get('user_id')
    print("user_id",user_id)
    carts = CartInfo.objects.filter(user_id=user_id)
    print("carts",carts)
    context = {
        'title':'购物车',
        'page_name': 1,
        'page_name_title': '购物车',
        'carts':carts

    }
    return render(request,'df_cart/cart.html',context)

@islogin
def add(request,gid,count):
    # 获取当前用户id
    user_id = request.session.get('user_id')
    carts = CartInfo.objects.filter(user_id=user_id,goods_id=gid)
    print("carts_add",carts)
    # 如果找得到，把count加进去
    if len(carts) >= 1:
        cart = carts[0]
        cart.count += int(count)
        cart.save()

    # 找不到，新建一个对象
    else:
        cart = CartInfo()
        cart.user_id = user_id
        cart.goods_id = gid
        cart.count = int(count)
        cart.save()
    result = CartInfo.objects.filter(user_id=user_id).count()
    return JsonResponse({'count':result})
@islogin
def edit(request,cart_id,count):
    try:
        cart = CartInfo.objects.get(id=cart_id)
        cart.count = int(count)
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': 1}
    return JsonResponse(data)

@islogin
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(id=cart_id)
        cart.delete()
        data = {'ok': 0 }
    except Exception as e:
        data = {'ok': 1}
    return JsonResponse(data)