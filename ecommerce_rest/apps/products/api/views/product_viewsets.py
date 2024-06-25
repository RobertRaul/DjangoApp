from rest_framework import viewsets
from apps.products.api.serializers.product_serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.users.authentication_mixins import Authenticate

#from rest_framework.permissions import IsAuthenticated
from apps.base.utils import validate_files

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    #TODO traemos JWT para esta clase, pero para todas las clases seriia tedioso importarlo 
    # permission_classes = (IsAuthenticated,)
    #TODO listado de productos, lo desactivamos, y usamos el get_queryset
    #queryset = ProductSerializer.Meta.model.objects.all()    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()        
    
    #Sobreescribimos el metodo listar
    def list(self,request):
        print("HOLA DESDE EL LISTADO")
        product_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(product_serializer.data,status = status.HTTP_200_OK)
    
    #TODO o POST 
    def post(self,request):
        #TODO forma BRUSCA de que la data que llega, pueda ser modificada  -- request.data._mutable =True
        #request.data._mutable =True
        #datos = request.data
        # El valor sera None si llega un String, sino, que sea la misma imagen
        #datos['image'] = None if type(datos['image']) == str else datos['image']
        #request.data._mutable =False
        
        #TODO funcions generalizada en base.utils.py 
        datos_modi = validate_files(request.data,'image')
        
        serializer = self.serializer_class(data = datos_modi)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully on VIEWSETS'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk = None):
        #TODO funcions generalizada en base.utils.py         
        if self.get_queryset(pk):
            datos_modi = validate_files(request.data,'image',True)
            product_serializer = self.serializer_class(self.get_queryset(pk),data =datos_modi)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully'},status = status.HTTP_204_NO_CONTENT)
        return Response({'message':'Product not found in database'},status = status.HTTP_400_BAD_REQUEST)
