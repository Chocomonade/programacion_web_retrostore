from django.contrib import admin
from .models import PerfilUsuario
from .models import Producto

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol')
    list_filter = ('rol',)
    search_fields = ('user__username', 'user__email')

from django.contrib import admin
from .models import Categoria, Producto, Cliente, DireccionDespacho, Orden, DetalleOrden

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(DireccionDespacho)
admin.site.register(Orden)
admin.site.register(DetalleOrden)

