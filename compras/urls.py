from rest_framework.routers import DefaultRouter
from .viewsets import (
    UsuarioViewSet,
    ProdutoViewSet,
    ListaCompraViewSet,
    ItemViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'listas', ListaCompraViewSet)
router.register(r'itens', ItemViewSet)
urlpatterns = router.urls
