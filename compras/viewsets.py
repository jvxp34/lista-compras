from rest_framework import viewsets

from .models import (
    Usuario,
    Categoria,
    Produto,
    ListaCompra,
    Item
)

from .serializers import (
    UsuarioSerializer,
    CategoriaSerializer,
    ProdutoSerializer,
    ListaCompraSerializer,
    ItemSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ListaCompraViewSet(viewsets.ModelViewSet):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer