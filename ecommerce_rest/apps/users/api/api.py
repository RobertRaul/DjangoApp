from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer,UserListSerializer,UserSerializerNoTodosLosCamposPUT,PasswordChangeSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

#TODO EMPEZAMOS A TRABAJAR XON VIEWSET

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    
    def get_object(self,pk):
        #return self.serializer_class().Meta.model.objects.get(id=pk).first()
        #return get_object_or_404(self.serializer_class().Meta.model,pk=pk)
        return get_object_or_404(self.model,pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            #queryset = self.serializer_class().Meta.model.objects.filter(is_active=True)
            self.queryset = self.serializer_class().Meta.model.objects.all().values('id','username','email','password')
        return self.queryset
    def list(self,request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users,many=True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    def create(self,request):
        user = self.serializer_class(data =request.data)
        if user.is_valid():
            user.save()
            return Response({'message': 'User Create Successfully'},status = status.HTTP_201_CREATED)
        return Response({'message': 'Errores duirante el registor','Error': user.errors},status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk =None):
        user = self.get_object(pk)
        users_serializer = self.serializer_class(user)
        return Response(users_serializer.data)

    def update(self,request,pk =None):
        user = self.get_object(pk)
        user_seriali= UserSerializerNoTodosLosCamposPUT(user,data=request.data)
        if user_seriali.is_valid():
            user_seriali.save()
            return Response({'message': 'User Update Successfully'},status = status.HTTP_200_OK)
        return Response({'message': 'Errores','error': user_seriali.errors},status = status.HTTP_400_BAD_REQUEST)
    #TODO eliminacion logica, iosea lo pondemos desactivado
    def destroy(self,request,pk =None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        #  user_destroy retorna un numero de registros afectados, si es = 1 entonces si lo afecto
        if user_destroy == 1:
            return Response({'message':'Usuario eliminado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'No encontrado','Errors': user_destroy.errors},status = status.HTTP_404_NOT_FOUND)
        
    #TODO creamos una ruta nueva, con el "actions", url_path para ponerle el nombre que queramos.
    # detail = True, agrega a la ruta que se pida un id ruta/{id}/cambiar_password
    @action(detail =True,methods = ['POST'],url_path='cambiar_password')
    def set_password(self,request,pk=None):
        user = self.get_object(pk)
        password_ser  = PasswordChangeSerializer(data=request.data)
        if password_ser.is_valid():
            user.set_password(password_ser.validated_data['pass1'])
            user.save()
            return Response({'message':'Contraseña actualizada'}, status=status.HTTP_200_OK )
        return Response({'message':'Hay enrrores','erros':password_ser.errors}, status=status.HTTP_400_BAD_REQUEST )
        












################################################################
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all().values('id','username','email','password')
        # TODO cuando se obtenga varios datos, se debe agregar many=True
        users_serializer = UserListSerializer(users,many=True) 
        return Response(users_serializer.data)

@api_view(['GET','POST'])
def user_api_view(request):
    #listado
    if request.method == 'GET':
        users = User.objects.all().values('id','username','email','password')
        # TODO cuando se obtenga varios datos, se debe agregar many=True
        users_serializer = UserListSerializer(users,many=True) 
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    #creation
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk):
    #TODO realizamos la consulta general
    user = User.objects.filter(id=pk).first()
    #TODO realizamos la validacion
    if user:
        #retrieve, find by id 
        if request.method == 'GET':            
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':            
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':            
            user.delete()
            return Response({'message': 'User deleted successfully'},status = status.HTTP_204_NO_CONTENT)
    return Response({'message': 'User not found'},status = status.HTTP_400_BAD_REQUEST)