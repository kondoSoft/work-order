from django.conf.urls import include, url
from .views import ApiWorkOrderList

urlpatterns = [
    url(r'^work/orders/$', ApiWorkOrderList.as_view(), name='api-work-orders-list'),
]
