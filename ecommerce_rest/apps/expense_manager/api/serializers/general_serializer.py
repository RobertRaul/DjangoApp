from rest_framework import serializers
from apps.expense_manager.models import Supplier,PaymentType,Voucher
from apps.products.models import Product

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ('created_date','modified_date','delete_date')
        
    def save(self):
        new_supplier = Supplier.objects.create(**self.validated_data)
        return new_supplier.to_dict()
    
class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ('id', 'name')
    
    
class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id', 'name')
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')
        
