from rest_framework import serializers
from .models import Usuario, Produto, ListaCompra, Item


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ListaCompraSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ListaCompra
        fields = "__all__"