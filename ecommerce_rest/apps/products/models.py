from django.db import models
from apps.base.models import BaseModel
# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion',max_length=50,blank=False,null=False,unique=True)    
    
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.description    

class CategoryProduct(BaseModel):
    description = models.CharField('Descripcion',max_length=50,blank=False,null=False,unique=True)        
    
    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    def __str__(self):
        return self.description

class Indicator(BaseModel):
    descount_value = models.PositiveIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name='Indicador de Oferta')    
            
    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Oferta de la Categoria {self.category_product} : {self.descount_value}%'    

class Product(BaseModel):
    name = models.CharField('Nombre de Producto',max_length=150,unique=True,blank=False,null=False)
    description = models.TextField('Description',blank=False,null= False)
    image = models.ImageField('Imagen del Producto', upload_to='products/',blank=True,null=True)
    measure_unit = models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name="Unidad de Medida",null=True)
    category_product = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name="Categoria de producto",null=True)    

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f'{self.name} - {self.description}'
