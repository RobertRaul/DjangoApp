from rest_framework import generics

#TODO generalizamos el generics.ListAPIView en esta clase, que podra ser heredada por las clases que lo requieran
class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None
        
    def get_queryset(self):
        #TODO get_serializer es un metodo que trae Meta.model, de esta manera se asocia con el modelo y realizamos el filter directamente alli
        #TODO La accion que se realiza es JERARQUIA del serializer, para no repetir codigo 
        model = self.get_serializer().Meta.model
        #return model.objects.filter(state=True)
        return model.objects.all()
    