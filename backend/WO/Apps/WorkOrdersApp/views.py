#encoding:utf-8
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import transaction
from django.contrib import messages
from .models import  Order, Status, OrderStatusPhoto
from .forms import NewOrderForm
from .utils import NeverCacheMixin

class DropZoneExample(TemplateView):
    "Example of dropzone usage"
    template_name = 'drop_zone_example.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print('the photo arrived!')
        return super(TemplateView, self).render_to_response(context)


class WorkOrdersListView(NeverCacheMixin, TemplateView):
    "Example of dropzone usage"
    template_name = 'work_orders_list.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print('the photo arrived!')
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(WorkOrdersListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        context['list_orders'] = 'active'
        context['work_orders'] = 'active'
        return context


class NewOrderView( NeverCacheMixin, CreateView):
    model = Order
    form_class = NewOrderForm
    template_name = 'new_orders_form.html'

    def get_success_url(self):
        return reverse('work-orders-list')


    @transaction.atomic()
    def form_valid(self, form):

        form.instance.user = self.request.user
        object_id = form.save
        messages.success(self.request,"Order created")

        return super(NewOrderView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewOrderView, self).get_context_data(**kwargs)
        context['work_orders'] = 'active'
        context['new_orders'] = 'active'
        return context


class DetailOrderView(NeverCacheMixin, DetailView):
    model = Order
    template_name = 'detail_order.html'


    def get_context_data(self, **kwargs):
        status_photo = self.request.GET.get('status_photo')
        status = Status.objects.filter(code__in = [6,7,4,8])
        order_status_photo = OrderStatusPhoto.objects.filter(order = self.object)
        if status_photo:
            order_status_photo = order_status_photo.filter(photo__status_id=status_photo)
        print(order_status_photo)
        context = super(DetailOrderView, self).get_context_data(**kwargs)
        context["list_orders"] = "active"
        context['work_orders'] = 'active'
        context['status'] = status
        context['order_status_photo'] = order_status_photo
        return context


class EditOrderView( NeverCacheMixin, UpdateView):
    model = Order
    form_class = NewOrderForm
    template_name = 'new_orders_form.html'

    def get_success_url(self):
        return reverse('work-orders-list')


    @transaction.atomic()
    def form_valid(self, form):
        object_id = form.save
        messages.success(self.request,"Edited order")

        return super(EditOrderView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditOrderView, self).get_context_data(**kwargs)
        context['work_orders'] = 'active'
        context['new_orders'] = 'active'
        return context