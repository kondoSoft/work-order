__author__ = 'jonatanmendez'
from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^$',Login.as_view(), name = 'login-view' ),
       url(r'^logout_user/$', Logout.as_view(), name='logout-user-view')
    ]