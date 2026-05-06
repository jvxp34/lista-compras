from rest_framework import serializers
from .models import (
    Usuario,
    Categoria,
    Produto,
    ListaCompra,
    Item
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(
        source='categoria.nome',
        read_only=True
    )

    class Meta:
        model = Produto
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(
        source='produto.nome',
        read_only=True
    )

    class Meta:
        model = Item
        fields = '__all__'


class ListaCompraSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ListaCompra
        fields = '__all__'