from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #TODO recordar que cada aplicacion que se cree, debe heredar el nombre del carpeta superior
    name = 'apps.users'
