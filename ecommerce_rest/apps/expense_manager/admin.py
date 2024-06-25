from django.contrib import admin

from apps.expense_manager.models import *
# Register your models here.

class SupplierDisplay(admin.ModelAdmin):
    list_display = ('id','ruc','business_name')
    
class VoucherDisplay(admin.ModelAdmin):
    list_display = ('id','name') 

class MermaDisplay(admin.ModelAdmin):
    list_display = ('id','date','product') 

class PaymentTypeDisplay(admin.ModelAdmin):
    list_display = ('id','name') 

admin.site.register(Supplier,SupplierDisplay)
admin.site.register(PaymentType,PaymentTypeDisplay)
admin.site.register(Voucher,VoucherDisplay)
admin.site.register(Expense)
admin.site.register(Merma,MermaDisplay)

