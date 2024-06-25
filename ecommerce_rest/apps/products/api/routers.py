from rest_framework.routers import DefaultRouter

from apps.products.api.views.product_viewsets import ProductViewSet
from apps.products.api.views.general_viewsets import *

router = DefaultRouter()
router.register(r'products',ProductViewSet,basename='products')
router.register(r'measure_unit_vs',ProductViewSet,basename='measure_unit')
router.register(r'indicator_vs',ProductViewSet,basename='indicator')
router.register(r'category_product_vs',ProductViewSet,basename='category_product')

urlpatterns = router.urls
