from django.http.response import HttpResponseRedirect

def islogin(func):
    def login_fun(request,*args,**kwargs):
        # 判断是否已经登录
        # 如果已经登录正常访问页面
        if request.session.get('user_id'):
            return func(request,*args,**kwargs)
        # 如果未登录重定向到登陆页面
        else:
            red = HttpResponseRedirect('/df_user/login')
        # 缓存路径,登录成功返回刚才访问的页面
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun