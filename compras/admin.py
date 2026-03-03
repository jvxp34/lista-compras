from django.contrib import admin
from .models import Usuario, Produto, ListaCompra, Item


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "is_active", "created_at")
    search_fields = ("name", "email")
    list_filter = ("is_active", "created_at")
    ordering = ("-created_at",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)
    ordering = ("name",)


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(ListaCompra)
class ListaCompraAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "usuario", "total", "created_at")
    search_fields = ("name", "usuario__name")
    list_filter = ("created_at", "usuario")
    ordering = ("-created_at",)
    inlines = [ItemInline]
    readonly_fields = ("total",)  # impede editar manualmente


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lista",
        "produto",
        "quantidade",
        "valor",
        "comprado",
        "created_at",
    )
    search_fields = ("produto__name",)
    list_filter = ("comprado", "lista")
    ordering = ("-created_at",)
