from django.conf.urls import include, url
from .views import DropZoneExample, WorkOrdersListView, NewOrderView, DetailOrderView, EditOrderView

urlpatterns = [
    url(r'^dropzone/$', DropZoneExample.as_view(), name='dropzone'),
    url(r'^work/orders/$', WorkOrdersListView.as_view(), name='work-orders-list'),
    url(r'^new/order/$', NewOrderView.as_view(), name='new-order'),
    url(r'^detail/order/(?P<pk>\d+)/$', DetailOrderView.as_view(), name='detail-order'),
    url(r'^edit/order/(?P<pk>\d+)/$', EditOrderView.as_view(), name='edit-order'),
]