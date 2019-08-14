from django.contrib import admin
from .models import GoodsInfo,TypeInfo
# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
    list_per_page = 10

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gkucun', 'gjianjie', 'gcontent', 'gtype']
    list_per_page = 15


admin.site.register(GoodsInfo,GoodsInfoAdmin)
admin.site.register(TypeInfo,TypeInfoAdmin)
