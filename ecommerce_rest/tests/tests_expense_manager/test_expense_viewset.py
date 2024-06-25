from tests.test_setup import TestSetUp
from tests.factories.expense_manager.expense_factories import SupplierFactory
from apps.expense_manager.models import Supplier
from rest_framework import status
class ExpenseTestCase(TestSetUp):
    #TODO Documentacion https://docs.python.org/3/library/unittest.html
    
    #TODO test para probar la busqueda de proveedores
    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        #llamamos a nuestra ruta que creamos
        #TODO self.client ---> es simular un cliente que consume nuestra api o rutas
        response = self.client.get(
            '/expenseGVS/expense/buscar_proveedor/',
            {
                'ruc_or_business_name': supplier.ruc   
            },
            format ='json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['ruc'],supplier.ruc)
        
    #TODO forzamos un error 
    
    def test_search_supplier_error(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            '/expenseGVS/expense/buscar_proveedor/',
            {
                'ruc_or_business_name': '99999877'   
            },
            format ='json'
        )
        # import pdb; # estudiarlo mas
        # pdb.set_trace()
        
        self.assertEqual(response.status_code, 400)
        self.assertNotEqual(supplier.ruc, '99999844')
        # esta informacion viene del viewset de supplier "expenses_viewsets" linea 27
        self.assertEqual(response.data['message'],'Errores durante la busqueda')
        
    def test_new_supplier(self):
        supplier = SupplierFactory().build_supplier_JSON()
        response = self.client.post(
            '/expenseGVS/expense/nuevo_proveedor/',            
            supplier,                        
            format ='json'
        )
        #TODO pause la ejecucion en el punto para realizar comandos y ver que paso
        #TODO como "response.data" "supplier" "supplier['ruc']"
        # import pdb; # estudiarlo mas
        # pdb.set_trace()
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 1)
        self.assertEqual(response.data['supplier']['ruc'],supplier['ruc'])