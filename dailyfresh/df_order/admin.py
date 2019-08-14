from django.contrib import admin
from .models import OrderDetailInfo,OrderInfo
# Register your models here.
class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_display = ["goods","order","price","count"]
    list_per_page = 10
    site_url = "http://127.0.0.1:8080/df_goods/"
class OrderInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["oid","ototal","user","oIsPay"]
admin.site.register(OrderDetailInfo,OrderDetailInfoAdmin)
admin.site.register(OrderInfo,OrderInfoAdmin)