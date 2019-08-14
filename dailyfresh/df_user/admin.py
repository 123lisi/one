from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["id","uname","upwd","uaddress"]
    list_per_page = 10
admin.site.register(UserInfo,UserInfoAdmin)