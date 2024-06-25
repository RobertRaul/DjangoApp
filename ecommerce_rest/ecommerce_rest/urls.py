"""
URL configuration for ecommerce_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#TODO renombramos la clase a views_old_token 
# from apps.users.views_old_token import Login,Logout,UserToken

#TODO nuevas views de JWT
from apps.users.views import LoginJWT,LogoutJWT

#TODO para que podamos trabajr con stactis files serve
from django.views.static import serve
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
    title="Documentacion de API 0.1",
    default_version='v1',
    description="Documentacion de API de Eccomerce",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="rarmejo@gmail.com"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
        
    #TODO swagger urlpatterns  https://github.com/axnsan12/drf-yasg?tab=readme-ov-file#installation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ####
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.urls')),    
    path('products/', include('apps.products.api.urls')),    
    #TODO uso de viewsets, con routers
    path('productsVS/', include('apps.products.api.routers')),
    path('userVS/', include('apps.users.api.routers')),        
    #TODO LOGIN CON restframework auth token
    #TODO renombramos la clase a views_old_token 
    #path('', Login.as_view(),name = 'login'),
    #path('logout/', Logout.as_view(),name = 'logut'),
    #path('refresh_token/', UserToken.as_view(),name = 'refresh_token'),
    
    #TODO traemos JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('loginjwt/', LoginJWT.as_view(),name = 'login'),
    path('logoutjwt/', LogoutJWT.as_view(),name = 'logut'),     
    
    #TODO expense manager
    path('expenseGVS/', include('apps.expense_manager.api.routers')),     
]

urlpatterns += [
    #TODO agregamos una ruta para que podamos ver los archivos media que se añadan
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
