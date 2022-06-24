from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image')
    exclude = ('thumbnail',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
