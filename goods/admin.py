from django.contrib import admin
from .models import Goods, Category

# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Goods, PackageAdmin)
admin.site.register(Category, CategoryAdmin)