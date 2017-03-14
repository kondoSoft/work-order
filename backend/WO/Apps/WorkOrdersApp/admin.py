from django.contrib import admin
from Apps.WorkOrdersApp.models import Status,Person,Order,Remark
from reversion.admin import VersionAdmin


@admin.register(Status)
class StatusModelAdmin(VersionAdmin):
    pass


@admin.register(Person)
class PersonModelAdmin(VersionAdmin):
    pass


@admin.register(Order)
class OrderModelAdmin(VersionAdmin):
    pass


@admin.register(Remark)
class RemarkModelAdmin(VersionAdmin):
    pass