from apps.products.models import MeasureUnit,CategoryProduct,Indicator
from rest_framework import serializers


#MeasureUnit,CategoryProduct,Indicator
class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('created_date','modified_date','delete_date')
        
class CategoryProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryProduct
        exclude = ('created_date','modified_date','delete_date')
        
class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('created_date','modified_date','delete_date')