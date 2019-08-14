from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.order),
    url('^add_order$',views.order_handle)

]