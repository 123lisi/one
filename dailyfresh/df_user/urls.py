from django.conf.urls import url
from . import views

urlpatterns = [
    url('^register$', views.register),
    url('^login$', views.login),
    url('^register_handle', views.register_handle),
    url('^register_exist',views.register_exist),
    url('^login_handle',views.login_handle),
    url('^info$',views.info),
    url('^order(\d+)$',views.order),
    url('^site$',views.site),
    url('^logout',views.logout),
    url('^email_send',views.email_send),
    url('^updatpwa',views.updatpwa),
    url('^deleteorder(\d+)',views.deleteorder),
]
