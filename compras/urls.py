from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    CategoriaViewSet,
    ProdutoViewSet,
    ListaCompraViewSet,
    ItemViewSet
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'listas', ListaCompraViewSet)
router.register(r'itens', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]