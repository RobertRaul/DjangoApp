from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
#TODO creamos nuestro serializador para nuestras pruebas con JWT
from apps.users.api.serializers import CustomTokenObtainPairSerializer,CustomUserJWTSerializer
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
#TODO creamos nuestra propia clase de LOGIN para JWT


class LoginJWT(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
            
    def post(self, request,*args,**kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        #TODO el metodo authenticate de django.contrib.auth verifica que exciste un usuari y contraseña iguale sen la base de datos
        user = authenticate(
            username = username,
            password = password
        )
        
        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserJWTSerializer(user)
                return Response({'token': login_serializer.validated_data.get('access'),
                                'refresh_token': login_serializer.validated_data.get('refresh'),
                                'user': user_serializer.data,
                                'message':'Login successful congratulations :D'},
                                status = status.HTTP_200_OK
                                )
            return Response({'Error':'Username or password incorrect, TRY AGAIN'},status = status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'Username or password incorrect, TRY AGAIN'},status = status.HTTP_400_BAD_REQUEST)
    

class LogoutJWT(GenericAPIView):
    #TODO falta su SERIALIZADOR
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user',0).first())
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'Success':'Sesion cerrado correctamente'},status = status.HTTP_200_OK)
        return Response({'Error':'No existe este usuario'},status = status.HTTP_400_BAD_REQUEST)
    