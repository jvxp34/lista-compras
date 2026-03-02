import django_filters
from .models import Usuario, Produto, ListaCompra, Item


# =========================
# Usuario Filter
# =========================
class UsuarioFilter(django_filters.FilterSet):

    created_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte"
    )

    created_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte"
    )

    class Meta:
        model = Usuario
        fields = ["is_active"]


# =========================
# Produto Filter
# =========================
class ProdutoFilter(django_filters.FilterSet):

    created_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte"
    )

    created_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte"
    )

    class Meta:
        model = Produto
        fields = ["is_active"]


# =========================
# ListaCompra Filter
# =========================
class ListaCompraFilter(django_filters.FilterSet):

    total_min = django_filters.NumberFilter(
        field_name="total",
        lookup_expr="gte"
    )

    total_max = django_filters.NumberFilter(
        field_name="total",
        lookup_expr="lte"
    )

    class Meta:
        model = ListaCompra
        fields = ["usuario"]


# =========================
# Item Filter
# =========================
class ItemFilter(django_filters.FilterSet):

    valor_min = django_filters.NumberFilter(
        field_name="valor",
        lookup_expr="gte"
    )

    valor_max = django_filters.NumberFilter(
        field_name="valor",
        lookup_expr="lte"
    )

    class Meta:
        model = Item
        fields = ["lista", "comprado"]