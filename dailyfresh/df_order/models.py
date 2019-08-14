from django.db import models
from datetime import datetime

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    odate = models.DateTimeField(default=datetime.now)
    oIsPay = models.IntegerField(default=0)
    ototal = models.DecimalField(max_digits=20, decimal_places=2)
    oaddress = models.CharField(max_length=150, default='')
    zhifu = models.IntegerField(default=0)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField()