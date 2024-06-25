from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from apps.expense_manager.models import (Supplier,Voucher,PaymentType)
from apps.expense_manager.api.serializers.expense_serializer import ExpenseSerializer
from apps.expense_manager.api.serializers.general_serializer import (
    SupplierSerializer,VoucherSerializer,PaymentTypeSerializer,ProductSerializer)
from apps.products.models import Product
#TODO importamos JWT para obtener el ID del usuario
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.base.utils import formatear_date
class ExpenseViewSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer
    
    @action(methods =['get'],detail = False,url_path='buscar_proveedor')
    def search_supplier(self,request): #buscar proveedor
        ruc_or_business_name = request.query_params.get('ruc_or_business_name','')
        supplier = Supplier.objects.filter(
            Q(ruc__iexact=ruc_or_business_name)| #  | = es un "or"
            Q(business_name__iexact=ruc_or_business_name)
            ).first()
        if supplier!=None:
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data, status = status.HTTP_200_OK)
        return Response({'message': 'Errores durante la busqueda'}, status = status.HTTP_400_BAD_REQUEST)                
    
    
    @action(methods=['post'],detail=False,url_path='nuevo_proveedor')
    def new_supplier(self,request):
        data_supplier = request.data
        data_supplier = SupplierSerializer(data =data_supplier)        
        if data_supplier.is_valid():
            data_supplier = data_supplier.save()
            print(data_supplier)
            return Response({'message':'Proveedor registrado correctamente','supplier':data_supplier}, status = status.HTTP_201_CREATED)
        return Response({'message': 'Errores durante el registro','Error': data_supplier.errors}, status = status.HTTP_400_BAD_REQUEST)                
    
    #Listado de Vouchers
    @action(methods=['post'],detail=False,url_path='vouchers')
    def get_vouchers(self,request):
        data = Voucher.objects.filter(state=True).order_by('id')
        data = VoucherSerializer(data,many=True).data
        return Response(data)
    
    #Listado de Tipos de Pago
    @action(methods=['post'],detail=False,url_path='tipos_pagos')
    def get_payment_type(self,request):
        data = PaymentType.objects.filter(state=True).order_by('id')
        data = PaymentTypeSerializer(data,many=True).data
        return Response(data)
    
    #Listado de Productos
    @action(methods=['post'],detail=False,url_path='productos')
    def get_products(self,request):
        data = Product.objects.filter(state=True).order_by('id')
        data = ProductSerializer(data,many=True).data
        return Response(data)
    
    #TODO funciona para formatear la data que nos llegues del request
    def format_dateee(self,data):
        data['data']=formatear_date(data['date'])
        return data
    
    #TODO registrar factura 
    def create(self,request):
        data = request.data
        #instanciamos JWT
        JWTauth = JWTAuthentication()
        #recuperamos el usuario de request, que llegaran forma de token, decode token
        usr, token =JWTauth.authenticate(request)
        data['user'] = usr.id
        
        #TODO podemos formatear la data que nos llega y luego enviarlo en el serializer class
        #new_data = self.format_dateee(request.data)
        # data = new_data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Factura registrada correctamente'
            },status = status.HTTP_201_CREATED)
        return Response({
                'message':'Errores durante el registro',
                'errors': serializer.errors
            },status = status.HTTP_400_BAD_REQUEST)