from rest_framework import generics,viewsets
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,IndicatorSerializer,CategoryProductSerializer

#TODO ya no heredamos de ListAPIView sino de, GeneralListAPIView que lo simplifica y evita duplicidad de codigo
class MeasureUnitListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    
class IndicatorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer    