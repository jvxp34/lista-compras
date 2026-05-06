from django.db import models
from django.db.models import Sum, F
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Usuario(BaseModel):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome


class Categoria(BaseModel):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'categorias'


    def __str__(self):
        return self.nome


class Produto(BaseModel):
    nome = models.CharField(max_length=120)

    categoria = models.ForeignKey(
        Categoria,
        related_name='produtos',
        on_delete=models.CASCADE,

    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome


class ListaCompra(BaseModel):
    nome = models.CharField(max_length=120)

    usuario = models.ForeignKey(
        Usuario,
        related_name='listas',
        on_delete=models.CASCADE
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'listas_compras'

    def __str__(self):
        return self.nome

    def atualizar_total(self):
        total = self.itens.aggregate(
            total=Sum(F('subtotal'))
        )['total'] or 0

        self.total = total
        self.save(update_fields=['total'])


class Item(BaseModel):
    lista = models.ForeignKey(
        ListaCompra,
        related_name='itens',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        Produto,
        related_name='itens',
        on_delete=models.CASCADE
    )

    quantidade = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )

    comprado = models.BooleanField(default=False)

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'itens'

        unique_together = ('lista', 'produto')

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.produto.preco

        super().save(*args, **kwargs)

        self.lista.atualizar_total()

    def delete(self, *args, **kwargs):
        lista = self.lista

        super().delete(*args, **kwargs)

        lista.atualizar_total()