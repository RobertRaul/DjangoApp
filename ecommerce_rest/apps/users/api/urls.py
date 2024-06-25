from django.contrib import admin
from django.urls import path
from apps.users.api.api import UserAPIView,user_api_view,user_detail_view

urlpatterns = [
    path('list/', UserAPIView.as_view(),name ='usuario_api'),
    path('list_view/', user_api_view,name ='usuario_api_view'),
    path('list_view/<int:pk>', user_detail_view,name ='user_detail_view'),
]
