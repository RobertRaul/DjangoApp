from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer
from rest_framework import generics,status
from rest_framework.response import Response

#TODO el ListAPIView y CreateAPIView se pueden unir en uno solo, gracias a rest_framework, con el nombnre ListCreateAPIView
class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer
#TODO el ListAPIView y CreateAPIView se pueden unir en uno solo, gracias a rest_framework, con el nombnre ListCreateAPIView
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    #TODO reescribimos el metodo post del serialiazdor, para mandar neustro mensaje de nosotros    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#TODO esta APIView trae GET (obtener),PUT 'actualizar', PATH 'traex data exacta', DELETE eliminar
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer    

    #TODO construimos el get_query set, cuando traiga un ID es busqueda, sino es listado completo
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    #TODO metodo que trae los datos del producto, de acuerdo al ID del producto
    def patch(self,request,pk = None):        
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response({'message': 'Product not founded in database'},status = status.HTTP_404_NOT_FOUND)
    
    #TODO sobreescribimos el metodo PUT que actualiza
    def put(self,request,pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    #TODO realizamos una eliminacion logica (pasamos el estado a False), modificar el metodo delete del serializer
    def delete(self, request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully'},status = status.HTTP_204_NO_CONTENT)
        return Response({'message':'Product not found in database'},status = status.HTTP_400_BAD_REQUEST)
  
    
    
    


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    #TODO 'ProductListCreateAPIView' should either include a `queryset` attribute, or override the `get_queryset()` method.
    #TODO tenemos que agregar el atributo "queryset"
    queryset = ProductSerializer.Meta.model.objects.all()
    
    #TODO  "get_queryset" es mucho mas escalable que el atributo "queryset"
    def get_queryset(self):
        return super().get_queryset()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    
#TODO el retrieve api view, es usado solo para lectura y representar la instancia de un modelo unico, SOLO GET
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    
    #Sobreesceribimos la funcion "get_queryset" para poner nuestros parametros
    def get_queryset(self): 
        return self.get_serializer().Meta().model.objects.all()
        #return self.get_serializer().Meta().model.objects.filter(state = True)         

#TODO RetrieveUpdate trae los metodos GET Y PUT en una sola view
class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    
    #Sobreesceribimos la funcion "get_queryset" para poner nuestros parametros
    def get_queryset(self): 
        return self.get_serializer().Meta().model.objects.all()
        #return self.get_serializer().Meta().model.objects.filter(state = True)     
    def put(self,request,pk= None):
        return Response({'Error':'Test request put is retrieve update view'})
        
        
        
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta().model.objects.all()
    
    #TODO realizamos una eliminacion logica (pasamos el estado a False), modificar el metodo delete del serializer
    def delete(self, request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully'},status = status.HTTP_204_NO_CONTENT)
        return Response({'message':'Product not found in database'},status = status.HTTP_400_BAD_REQUEST)
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self,pk = None):
        return self.get_serializer().Meta().model.objects.filter(id=pk).first()
        #return self.get_serializer().Meta().model.objects.filter(id=pk).filter(state= True).first()
    
    #TODO metodo que trae los datos del producto, de acuerdo al ID del producto
    def patch(self,request,pk = None):        
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response({'message': 'Product not founded in database'},status = status.HTTP_404_NOT_FOUND)
    
    #TODO sobreescribimos el metodo PUT que actualiza
    def put(self,request,pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)