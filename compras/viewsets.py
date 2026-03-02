from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Usuario, Produto, ListaCompra, Item
from .serializers import (
    UsuarioSerializer,
    ProdutoSerializer,
    ListaCompraSerializer,
    ItemSerializer
)
from .filters import (
    UsuarioFilter,
    ProdutoFilter,
    ListaCompraFilter,
    ItemFilter
)


# =========================
# Usuario
# =========================
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = UsuarioFilter
    search_fields = ["name", "email"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


# =========================
# Produto
# =========================
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProdutoFilter
    search_fields = ["name"]
    ordering_fields = ["created_at", "name"]
    ordering = ["name"]


# =========================
# ListaCompra
# =========================
class ListaCompraViewSet(ModelViewSet):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ListaCompraFilter
    search_fields = ["name"]
    ordering_fields = ["created_at", "total"]
    ordering = ["-created_at"]


# =========================
# Item
# =========================
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ItemFilter
    search_fields = ["produto__name"]
    ordering_fields = ["valor", "quantidade", "created_at"]
    ordering = ["-created_at"]