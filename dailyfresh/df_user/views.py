from hashlib import sha1
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, JsonResponse
from .models import UserInfo
from .islogin import islogin
from df_goods.models import *
from df_order.models import OrderDetailInfo,OrderInfo
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.
def register(request):
    context = {
        'title': '注册'
    }
    return render(request, 'df_user/register.html', context)


def login(request):
    uname = request.session.get('uname', '')
    context = {
        'title': '登录',
        'user_error': 0,
        'pwd_error': 0,
        'uname': uname

    }
    return render(request, 'df_user/login.html', context)


def register_handle(request):
    # 接收用户提交的信息
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    # 判断用户两次输入的密码是否一致
    if ucpwd != upwd:
        return HttpResponseRedirect('/df_user/register')

    # 创建sha1的对象
    # 对pwd进行加密
    s1 = sha1()
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()

    # 创建对象，保存到数据库中
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()

    return HttpResponseRedirect('/df_user/login')


def register_exist(request):
    # 通过ajax提交请求，检查用户名是否存在
    get = request.GET
    uname = get.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login_handle(request):
    # 接收用户提交的信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    reme = post.get('remember')

    users = UserInfo.objects.filter(uname=uname)
    if len(users) >= 1:
        # 对输入的密码进行加密，与原密码进行匹配
        s1 = sha1()
        s1.update(upwd.encode())
        upwd2 = s1.hexdigest()

        # 密码相同
        if upwd2 == users[0].upwd:
            url = request.COOKIES.get('url', '/df_user/info')
            # 登录成功,缓存到cookies和session中
            red = HttpResponseRedirect(url)
            if reme:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '')

            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red

        # 密码不同
        else:
            context = {
                'title': '登录',
                'user_error': 0,
                'pwd_error': 1,
                'uname': uname
            }
            return render(request, 'df_user/login.html', context)
    else:
        context = {
            'title': '登录',
            'user_error': 1,
            'pwd_error': 0,
            'uname': uname
        }
        return render(request, 'df_user/login.html', context)


@islogin
def info(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=user_id)
    uname = user.uname
    ushou = user.ushou
    uaddress = user.uaddress

    # 从cookies中拿到数据
    goods_ids = request.COOKIES.get('goods_ids')
    # goods_ids 不为空
    if goods_ids and goods_ids != '':
        # 分割成列表
        goods_ids = goods_ids.split(',')
    else:
        goods_ids = []
    # 通过id拿到每个产品
    goods_list = []
    for id in goods_ids[:4]:
        if id != '':
            try:
                goods = GoodsInfo.objects.get(id=id)
                goods_list.append(goods)
            except :
                pass
            

    context = {
        'title': '用户中心',
        'uname': uname,
        'ushou': ushou,
        'uaddress': uaddress,
        'info': 1,
        'page_name': 1,
        'page_name_title': '用户中心',
        'goods_list':goods_list,
    }
    return render(request, 'df_user/user_center_info.html', context)


@islogin
def order(request,pageid):
    user_id = request.session.get('user_id')
    orders = OrderInfo.objects.filter(user=user_id)
    # print(orders[0].oIsPay)
    for order in orders:
        order_skus = OrderDetailInfo.objects.filter(order_id= order.oid).order_by('-id')
        for order_sku in order_skus:
            #计算小计
            amount =order_sku.price * order_sku.count
            #动态增加属性
            order_sku.amount = amount
        #动态增加属性
        order.order_skus = order_skus
    # 分页
    paginator = Paginator(orders,1)
    # 根据pageid确定第几页
    pageGoods = paginator.page(int(pageid))
    # 所有页的id
    indexList = paginator.page_range
    context = {
        'title': '用户中心',
        'order': 1,
        'pageid': int(pageid),
        'page_name_title': '用户中心',
        'detail':pageGoods,
        'indexList':indexList,
        'page_name': 1

    }
    return render(request, 'df_user/user_center_order.html', context)


@islogin
def site(request):
    # 获取当前用户id
    user_id = request.session.get('user_id')
    # 获取当前用户
    user = UserInfo.objects.get(id=user_id)

    # 如果用户通过post请求数据
    if request.method == 'POST':
        post = request.POST
        user.uaddress = post.get('uaddress')
        user.ushou = post.get('ushou')
        # user.uyoubian = post.get('uyoubian')
        user.uname = post.get('uname')
        user.save()

    # 传3个参数
    # uaddress = user.uaddress
    # uname = user.uname
    # ushou = user.ushou

    context = {
        'title': '用户中心',
        'site': 1,
        # 'uaddress':uaddress,
        # 'uname':uname,
        # 'ushou':ushou,
        'user': user,
        'page_name': 1,
        'page_name_title': '用户中心',

    }
    return render(request, 'df_user/user_center_site.html', context)

#发送邮件
def email_send(request):
    return render(request, 'df_user/updateEmail.html', {"ok":0})
def updatpwa(request):
    get = request.GET
    email = get.get("email")
    title = "你好"
    send_mail(title,'Here is the message.', '361789224@qq.com',[email])
    return render(request, 'df_user/login.html', {"ok":0})
def logout(request):
    # 清理session缓存
    request.session.flush()
    return HttpResponseRedirect('/df_user/login')
def deleteorder(request,pageid):
    user_id = request.session.get('user_id')
    orders = OrderInfo.objects.filter(user=user_id)
    order_get = request.GET
    order_id = order_get.get("order_id")
    
    infos = OrderDetailInfo.objects.filter(order_id= order_id)
    print(infos)
    for info in infos:
        dingdan = OrderInfo.objects.filter(ototal= info.order.ototal)
        dingdan.delete()
    infos.delete()
    # print(orders[0].oIsPay)
    return HttpResponseRedirect("/df_user/order1")