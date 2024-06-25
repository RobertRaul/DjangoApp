from apps.users.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class Authenticate(object):
    #TODO creamos 2 variables, usuario: para saber que usuario estas haciendo la peticion
    #TODO creamos 2 variables, user_token_is_expired: para obtener el si esta expirado o no el token    
    user = None
    user_token_is_expired = False
    
    
    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()                                
                print(token)                
            except:
                return None
            #verifacion el token activo y si es correcto
            token_expire = ExpiringTokenAuthentication()        
            #TODO recuperramos los 4 campos que nos envian el meotod authenticate_credentials
            message, token,user,self.user_token_is_expired = token_expire.authenticate_credentials(token)     
            if user!=None and token!=None:
                self.user = user
                return user
            return message
        return None
    
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        #TODO si el metodo gget_user rotorna un valor, quiere decir que se encontro un token en el request
        if user is not None:
            #TODO quiere decir que retorno un mensaje, ya que el typo es STRING
            if type(user) == str:
                response = Response({'MsgError':user,'Token Expired': self.user_token_is_expired},status=status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            #TODO agregamos esta validacion, SI EL TOKEN ESTA VENCIDO, NO RECUPERA NADA, SE GENERA NUEVO TOKEN PARA LA SOLICITUD
            if not self.user_token_is_expired:
                return super().dispatch(request, *args, **kwargs)
        #TODO un Response no funciona en clases directas como dispatch, para ello de le pasa directamente 3 parametros adicionales
        response = Response({'Error':'No nse envio las credenciales','Token Expired': self.user_token_is_expired},status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response
    