from django.contrib import admin
from .models import Category, Store, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category, CategoryAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    list_filter = ('address',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Store, StoreAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Product, ProductAdmin)
