from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.cart),
    url('^add(\d+)_(\d+)',views.add),
    url('^edit(\d+)_(\d+)',views.edit),
    url('^delete(\d+)',views.delete)

]
