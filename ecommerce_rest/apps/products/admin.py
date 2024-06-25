from django.contrib import admin
from apps.products.models import *
# Register your models here.
#TODO modificamos los campos  que queremos motrar en el panel django, herando de admin.ModelAdmin
class MeasureUnitAdminListDisplay(admin.ModelAdmin):
    list_display = ('id','description')
class CategoryProductListDisplay(admin.ModelAdmin):
    list_display = ('id','description')
    
class ProductListDisplay(admin.ModelAdmin):
    list_display = ('id','name','description')

admin.site.register(MeasureUnit,MeasureUnitAdminListDisplay)
admin.site.register(CategoryProduct,CategoryProductListDisplay)
admin.site.register(Indicator)
admin.site.register(Product,ProductListDisplay)
