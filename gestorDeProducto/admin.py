from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import Marca
from .models import Tipo
from .models import Anime
from .models import Sucursal


class administradorProducto(admin.ModelAdmin):
    list_display = ['codigo_producto', 'nombre', 'marca', 'tipo', 'anime']
    list_filter = ['codigo_producto'] #mejorar el filtro por lista
    search_fields = ['codigo_producto', 'nombre']


admin.site.register(Producto, administradorProducto)


class administradorMarca(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter = ['nombre'] #mejorar el filtro por lista
    search_fields = ['nombre']


admin.site.register(Marca, administradorMarca)


class administradorTipo(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter = ['nombre'] #mejorar el filtro por lista
    search_fields = ['nombre']


admin.site.register(Tipo, administradorTipo)

admin.site.register(Sucursal)

class administradorAnime(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre'] #mejorar el filtro por lista
    search_fields = ['nombre']


admin.site.register(Anime, administradorAnime)