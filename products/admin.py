from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'imagen_preview',]

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-width: 100px;max-height: 100px"/>', obj.imagen.url)
        else:
            return 'No image'

admin.site.register(Product, ProductAdmin)
# Register your models here.

# style="max-with=100px;max-heigh=100px;max-width: 100px;max-height: 100p