from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

        
#TODO CREAMOS UN NUEVO SERIALIZADOR PARA JWT TOKEN

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserJWTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')
################################

class PasswordChangeSerializer(serializers.Serializer):
    pass1 = serializers.CharField(max_length=128,min_length=6,write_only=True)
    pass2 = serializers.CharField(max_length=128,min_length=6,write_only=True)
    
    def validate(self,value):
        if value['pass1'] != value['pass2']:
            raise serializers.ValidationError({
                'password':'Debe ingresar ambas contraseñas iguales'
            })
        return value
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #['name', 'email', 'first_name', 'last_name]   
    
    #TODO cosbreescribimos el metodo GUARDAR POST del serializador y encriptamos la contraseña que nos envian
    def create(self, validated_data):
        user = User(**validated_data) 
        user.set_password(validated_data['password'])
        user.save() 
        return user
    
    #TODO cosbreescribimos el metodo ACTUALIZAR PUT del serializador y encriptamos la contraseña que nos envian
    def update(self,instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
    
    
class UserSerializerNoTodosLosCamposPUT(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'last_name']           
    
    #TODO cosbreescribimos el metodo ACTUALIZAR PUT del serializador y encriptamos la contraseña que nos envian
    def update(self,instance, validated_data):
        update_user = super().update(instance, validated_data)
        #update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    #TODO esta funcion le pertenece a "serializers", la sobreescribimos y 
    #TODO de esa manera, podemos mostrar los campos que necesitemos
    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],            
            'password': instance['password'],            
        }
        
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')
