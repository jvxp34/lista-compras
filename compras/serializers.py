from rest_framework import serializers
from django.contrib.auth import authenticate
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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Usuário ou senha inválidos")

        if not user.is_active:
            raise serializers.ValidationError("Usuário inativo")

        data['user'] = user
        return data