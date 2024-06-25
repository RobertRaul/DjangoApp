from rest_framework import generics
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,IndicatorSerializer,CategoryProductSerializer

#TODO ya no heredamos de ListAPIView sino de, GeneralListAPIView que lo simplifica y evita duplicidad de codigo
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer
    
class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer    