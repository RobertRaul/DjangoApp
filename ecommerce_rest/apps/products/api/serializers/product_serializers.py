from apps.products.models import Product
from rest_framework import serializers

#TODO metodo 1, para recuperar la descripcion de los campos relacionados como categoria y unidad de medida
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    
    #TODO metodo 1: utilizamos los serializadores, traera la informacion completa del modelo relacionado
    #measure_unit = MeasureUnitSerializer()
    #category_product = CategoryProductSerializer()
    #TODO: metodo 2: recupera la data que se haya colocado en el modelo, __str__(self) return self.descripcion
    #measure_unit = serializers.StringRelatedField()
    #category_product = serializers.StringRelatedField()
            
    class Meta:
        model = Product
        exclude = ('created_date','modified_date','delete_date')
    
    #TODO validaciones a campos especificos y que non esten vacios
    def validate_measure_unit(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debe ingresar una unidad de medida')
        return value
    def validate_category_product(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debe ingresar una categoria')
        return value
    
    #TODO en el modelo no esta obligatorio estos 2 campos, pero con el metodo validate, los obligamos a solicitar
    def validate(self,data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({
                "measure_unit": "Debe ingresar una unidad de medida"
            })
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({
                "category_product": "Debe ingresar una Categoria de Producto"
            })
        return data
        
    #TODO: metodo 3, sobreescrobimos el metodo to_representation del serializador, para agregar lo que queremos mostrar
    def to_representation(self,instance):
        return {
            "id": instance.id,
            "state": instance.state,
            "name": instance.name,
            "description": instance.description,
            #"image": instance.image if instance.image != '' else '',
            #"image": instance.image or "",
            "image": instance.image.url if instance.image != '' else '',
            "measure_unit": instance.measure_unit.description if instance.measure_unit is not None else '',
            "category_product": instance.category_product.description if instance.measure_unit is not None else ''
            #"created_date" : instance.created_date
        }