from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}>"


class Usuario(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name


class Produto(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class ListaCompra(BaseModel):
    name = models.CharField(max_length=128)
    usuario = models.ForeignKey(Usuario, related_name='listas', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'lista_compra'
        verbose_name = 'Lista de Compra'
        verbose_name_plural = 'Listas de Compras'

    def __str__(self):
        return self.name

    def atualizar_total(self):
        total = 0
        for item in self.itens.all():
            total += item.quantidade * item.valor

        self.total = total
        self.save(update_fields=["total"])


class Item(BaseModel):
    lista = models.ForeignKey(ListaCompra, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    comprado = models.BooleanField(default=False)

    class Meta:
        db_table = 'item'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.lista.atualizar_total()

    def delete(self, *args, **kwargs):
        lista = self.lista
        super().delete(*args, **kwargs)
        lista.atualizar_total()