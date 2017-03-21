from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from  Apps.WorkOrdersApp.models import Order
from Apps.WorkOrdersApp.utils import NeverCacheMixin

class ApiWorkOrderList(NeverCacheMixin, BaseDatatableView):
    # The model we're going to show
    model = Order

    # define the columns that will be returned
    columns = ['id','start_date', 'end_date', 'coordinator', 'status', 'number','state','address','client','client_contract','vendor','vendor_sub_out','sub_out','']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['id','start_date', 'end_date', 'coordinator', 'status', 'number','state','address','client','client_contract','vendor','vendor_sub_out','sub_out','']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'coordinator':
            return '{0} {1}'.format(row.coordinator.first_name, row.coordinator.last_name)
        if column == 'client':
            return '{0} {1}'.format(row.client.first_name, row.client.last_name)
        if column == 'vendor':
            return '{0} {1}'.format(row.vendor.first_name, row.vendor.last_name)
        if column == 'status':
            return '{0}'.format(row.status.description)
        else:
            return super(ApiWorkOrderList, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get(u'sSearch', None)
        if search:
            qs = qs.filter(Q(start_date__istartswith=search)|Q(end_date__istartswith=search)|Q(coordinator__first_name__istartswith=search)|Q(coordinator__last_name__istartswith=search)|Q(status__description__istartswith=search)
                           |Q(number__istartswith=search)|Q(state__istartswith=search)|Q(address__istartswith=search)|Q(client__first_name__istartswith=search)|Q(client__last_name__istartswith=search)|Q(client_contract__istartswith=search)
                           |Q(vendor__first_name__istartswith=search)|Q(vendor__last_name__istartswith=search)|Q(vendor_sub_out__istartswith=search)|Q(sub_out__istartswith=search))

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get(u'customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
