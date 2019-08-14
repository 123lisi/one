from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^index$', views.index),
    url('^list(\d+)_(\d+)_(\d+)$',views.goodlist),
    url('^(\d+)$',views.detail)

]
