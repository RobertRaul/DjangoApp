from faker import Faker

from apps.expense_manager.models import Supplier

faker = Faker()

#TODO creamos una clase para crear data falsa con FAKER 
class SupplierFactory:
    #Creando la data con faker
    def build_supplier_JSON(self):
        return {
            'ruc':str(faker.random_number(digits=11)),
            'business_name':faker.company(),
            'address':faker.address(),
            'phone':str(faker.random_number(digits=11)),
            'email':faker.email(),
        }
        
    def create_supplier(self):
        return Supplier.objects.create(**self.build_supplier_JSON())
    
    
    
    ##
    ## https://pytest-with-eric.com/pytest-advanced/pytest-django-restapi-testing/#Unit-Tests-using-Pytest-Django
    
    #