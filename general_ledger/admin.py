from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'invoice_id',
    'supplier','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status',  'invoice_id','supplier',)


class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'invoice_id',
    'supplier','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status',  'invoice_id','supplier',)


class AccountsPayablesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'payment_id', 'accnt_payables_id',
     'supplier_institution','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status', 'payment_id', 'accnt_payables_id','supplier_institution',)

class BankAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'transaction_id',
     'bank_reciept_id','bank','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status',  'transaction_id',
     'bank_reciept_id', 'bank',)

class AccountsRecievableAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'invoice_id',
     'sales_id','customer','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status',  'invoice_id', 'customer',)

class CreditorsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'payment_id', 'invoice_id',
     'supplier','description', 'amount', 'account_dr', 'account_cr',]
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status', 'payment_id', 'invoice_id', 'supplier',)

class PurchasesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','department', 'user_status', 'invoice_id',
    'stock_accnt_inv_id', 'supplier','description', 'amount', 'account_dr', 'account_cr', 'due_date']
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)
    list_editable = ('user_status', 'invoice_id', 'stock_accnt_inv_id', 'supplier',)


class OpeningBalanceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','user_status', 'department', 'customer_institution','description', 'amount', 'account']
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department', 'account')

class IncomeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'employee','user_status', 'department', 'customer_institution','description', 'amount', 'account_dr', 'account_cr']
    search_fields = ['description__startswith', 'user_status__startswith', 'department__startswith']
    list_display_links = ['id', 'created_at', 'department', 'description', 'amount',]
    list_per_page =25
    list_filter = ('created_at', 'department',)

admin.site.register(OpeningBalance, OpeningBalanceAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(Creditors, CreditorsAdmin)
admin.site.register(AccountsRecievable, AccountsRecievableAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(AccountsPayables, AccountsPayablesAdmin)
admin.site.register(Expense, ExpenseAdmin)
