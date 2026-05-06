from django.contrib import admin

from .models import (
    Usuario,
    Categoria,
    Produto,
    ListaCompra,
    Item
)

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(ListaCompra)
admin.site.register(Item)