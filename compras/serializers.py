from rest_framework import serializers
from django.contrib.auth.models import User
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
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    categoria_nome = serializers.CharField(source='produto.categoria.nome', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'



class ListaCompraSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ListaCompra
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário ou senha inválidos")

        user = authenticate(username=user.username, password=password)

        if not user:
            raise serializers.ValidationError("Usuário ou senha inválidos")

        return {
            'user': user
        }