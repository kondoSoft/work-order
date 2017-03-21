from django.contrib import admin
from Apps.WorkOrdersApp.models import Status,Person,Order,Remark,RemarkStatusOrder,Photo,OrderStatusPhoto,Document,OrderStatusDocument
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


@admin.register(RemarkStatusOrder)
class RemarkStatusOrderModelAdmin(VersionAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(VersionAdmin):
    pass


@admin.register(OrderStatusPhoto)
class OrderStatusPhotoModelAdmin(VersionAdmin):
    pass


@admin.register(Document)
class DocumentModelAdmin(VersionAdmin):
    pass


@admin.register(OrderStatusDocument)
class OrderStatusDocumentModelAdmin(VersionAdmin):
    pass