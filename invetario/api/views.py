from rest_framework import viewsets
from invetario.api.serializers import ProductoSerializer
from invetario.models import Producto


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer