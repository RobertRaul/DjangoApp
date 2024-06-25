from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

#TODO clase principal para realizar el login y luego de ello tener el usuario
class TestSetUp(APITestCase):
    
    def setUp(self):
        from apps.users.models import User
        
        faker = Faker()
        
        self.login_url = '/loginjwt/'
        self.user = User.objects.create_superuser(
            name = 'developer',
            last_name = 'Robert Raul',
            username = faker.name(),
            password = '123456',
            email = faker.email()
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': '123456'
            },
            format = 'json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)        
        return super().setUp()
    
    #TODO para probar que funciona la funcion setUp
    # def test_cualquiercosa(self):
    #     pass