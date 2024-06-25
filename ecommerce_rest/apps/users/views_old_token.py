from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from apps.users.api.serializers import UserTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView

class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user=
            UserTokenSerializer().Meta.model.objects.filter(username=username).first()
            )
            return Response({'Token': user_token.key})
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas'
            },status = status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer =self.serializer_class(data = request.data,context = {'request':request})
        if login_serializer.is_valid():
            #recuperamos el usuario que se valido
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)                  
                #SI EL TOKEN ESTA CREADO
                if created:                      
                    return Response({'token': token.key, 
                            'user': user_serializer.data,
                            'message': 'Inicio de Sesion Exitoso'},status= status.HTTP_201_CREATED)  
                #si el token ya esta CREADO procedemos a eliminarlo para crear uno nuevo y mostrarlo
                else:
                    #TODO funcion que elimina un TOKEN y la sesion ACTUAL cuando se ingresa de nuevo al sistema
                    # #recuperamos las sesiones que esten abiertas
                    # all_sessions = Session.objects.filter(expire_date__gte =  datetime.now())       
                    # # una vez que tengamos las sesiones abiertas procedemos a eliminar la ultima que haya,
                    # #de esa manera solo quedara un acceso  
                    # if all_sessions.exists():
                    #     for session in all_sessions:
                    #         session_data = session.get_decoded()
                    #         if user.id == int(session_data.get('_auth_user_id')):
                    #             session.delete()                    
                    # token.delete()
                    # token = Token.objects.create(user=user)
                    # return Response({'token': token.key, 
                    #         'user': user_serializer.data,
                    #         'message': 'Inicio de Sesion Exitoso'},status= status.HTTP_201_CREATED) 
                    
                    #TODO si ya esta iniciado sesion no permite pasar, deberia cerrarse la sesion
                    token.delete()
                    return Response({'mensaje': 'Ya se tiene una sesion abierta con este usuario'},status= status.HTTP_401_UNAUTHORIZED)    
            else:
                return Response({'mensaje': 'Usuario Desactivado'},status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'mensaje': 'User or password incorrects'},status= status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'Hola desde el Response Final'},status= status.HTTP_200_OK)
        

class Logout(APIView):
    
    def get(self,request,*args,**kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte =  datetime.now())       
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()             
                token.delete()
                session_message = 'Sesiones de usuario eliminadas'            
                token_message = 'Token Eliminado'
                return Response({'token_message':token_message, 'session_message':session_message},status = status.HTTP_200_OK)
            return Response({'Error:':'User not found with this credentials'},status = status.HTTP_400_BAD_REQUEST)                
        except Exception as e:
            return Response({'Error:':'Not Found TOKEN is the request'},status = status.HTTP_400_BAD_REQUEST)



