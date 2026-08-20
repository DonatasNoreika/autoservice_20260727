from django.contrib import admin
from .models import Service, Car, Order, OrderLine, OrderComment

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    fields = ['service', 'qty', 'service_price', 'line_sum']
    readonly_fields = ['line_sum', 'service_price']


class OrderCommentInLine(admin.TabularInline):
    model = OrderComment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'total', 'deadline', 'client', 'status', 'is_overdue']
    inlines = [OrderLineInLine, OrderCommentInLine]
    readonly_fields = ['date', 'total']

    fieldsets = [
        ('General', {'fields': ('car', 'date', 'total', 'deadline', 'client', 'status')}),
    ]


class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'license_plate', 'vin_code', 'client_name']
    list_filter = ['make', 'model', 'client_name']
    search_fields = ['license_plate', 'vin_code']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
