from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime,timedelta,timezone
from django.conf import settings
from django.utils import timezone

class ExpiringTokenAuthentication(TokenAuthentication):
    #TODO creamos una variable que nos dara el estado del TOKEN, si expiro o no
    is_expired = False
    
    #TODO funcion que calcula EL TIEMPO DE EXPIRACION
    def expires_in(self,token):
        time_elapsed = timezone.now() - token.created
        lefT_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return lefT_time
    
    #TODO funcion que retorna si el token a expirado, ya que compara valores
    def is_token_expired(self,token):
        return self.expires_in(token)  < timedelta(seconds= 0)      
    
    #TODO Creamos varible que menciona si expiro o no, llamando a la funcion is_token_expired
    def token_expire_handler(self,token):
        is_expire = self.is_token_expired(token)
        #TODO si el token expiro, podemos crearlo uno nuevo
        if is_expire:
            #TODO recuperamos el usuario, eliminamos el token y luego le creamos unos nuevo
            #TODO cambiamos el estado del is_expired a TRUE ya que su token ha expirado
            self.is_expired= True
            user=token.user
            token.delete()
            token = self.get_model().objects.create(user=user)                        
        return is_expire
    

    #
    def authenticate_credentials(self,key):
        message,token,user = None,None,None
        try:
            #token = self.get_model().objects.get(key=key)        
            token = self.get_model().objects.select_related('user').get(key=key)    
            user = token.user    
        except self.get_model().DoesNotExist:
            message = 'Token Invalido'      
            self.is_expired= True      
            #raise AuthenticationFailed('Token Invalid')
        if token is not None:
            if not token.user.is_active:
                #raise AuthenticationFailed('Usuario no activo o eliminado')
                msg = 'Usuario no activo o eliminado'            
        
            is_expired = self.token_expire_handler(token)
            if is_expired:
                #raise AuthenticationFailed('Su token a expirado')
                msg = 'Su token a expirado'            
                
        
        return (message, token,user,self.is_expired)