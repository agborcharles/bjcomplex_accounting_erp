from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class BakeryReturnAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee', 'order_no','invoice_id','customer_from','return_id','customer_to',
    'department', 'sub_department','category', 'product', 'qty', 'cost_price', 'total_amount', ]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at','customer_from','customer_to', 'department', 'sub_department',
    'category', 'product']
    list_per_page =200
    list_filter = ('created_at', 'department', 'customer_from','customer_from','department', 'sub_department','category', 'product')
    list_editable = ( 'invoice_id', 'return_id',)


class BakeryOpeningBalancesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','openingbalance_id','customer',
    'department', 'amount',
    ]
    search_fields = ['customer__startswith', ]
    list_display_links = ['id', 'created_at', 'customer', 'department',]
    list_per_page =200
    list_filter = ('created_at', 'department', 'customer',)
    list_editable = ('amount',)


class BakeryPaymentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','collector','payment_id', 'session','customer',
    'department', 'amount',
    ]
    search_fields = ['customer__startswith', 'collector__startswith',]
    list_display_links = ['id', 'created_at', 'customer', 'department',]
    list_per_page =200
    list_filter = ('created_at', 'department','customer',)
    list_editable = ( 'payment_id', 'amount')

class BakeryCollectorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'collector',]



class BakerySalesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','invoice_id','supplier','customer',
    'session', 'category', 'product', 'qty', 'cost_price', 'total_amount', 'discount',
    'discount_value', 'net_amount', 'commission']
    search_fields = ['customer__startswith', 'product__startswith', 'supplier__startswith']
    list_display_links = ['id', 'created_at', 'supplier','customer', 'category', 'product']
    list_per_page =50
    list_filter = ('created_at', 'department', 'supplier','customer',
    'category', 'product')
    list_editable = ( 'invoice_id',)


admin.site.register(BakeryReturn, BakeryReturnAdmin)
admin.site.register(BakeryOpeningBalances, BakeryOpeningBalancesAdmin)
admin.site.register(BakeryPayment, BakeryPaymentAdmin)
admin.site.register(BakeryCollector, BakeryCollectorAdmin)
admin.site.register(BakerySales, BakerySalesAdmin)
