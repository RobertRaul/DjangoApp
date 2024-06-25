from django.contrib import admin
from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView ,IndicatorListAPIView,CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListAPIView,ProductCreateAPIView,ProductRetrieveAPIView,ProductDestroyAPIView,ProductUpdateAPIView,ProductListCreateAPIView,ProductRetrieveUpdateAPIView,ProductRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(),name ='measure_unit'),    
    path('indicator/', IndicatorListAPIView.as_view(),name ='indicator'),    
    path('category_product/', CategoryProductListAPIView.as_view(),name ='category_product'),    
    ################################################################################################
    path('product/list/', ProductListAPIView.as_view(),name ='product_list'),    
    path('product/create/', ProductCreateAPIView.as_view(),name ='product_create'),        
    path('product/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(),name ='product_retrieve'),    
    path('product/retrieve_update/<int:pk>', ProductRetrieveUpdateAPIView.as_view(),name ='product_retrieve_update'),        
    path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(),name ='product_destroy'),    
    path('product/update/<int:pk>', ProductUpdateAPIView.as_view(),name ='product_update'),        
    path('product/list_create/', ProductListCreateAPIView.as_view(),name ='product_listcreate'),
    ################################################################    
    path('product/product_retrieve_update_delete/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(),name ='product_retrieve_update_delete'),                 
]
