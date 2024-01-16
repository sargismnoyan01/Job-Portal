from django.contrib import admin
from .models import (HomeCarusel, HomeCaruselActive,
                    Category, Sub_Category, Product, Panel, ProductType,
                    HomeLogo, Contact, Cart)
# Register your models here.

@admin.register(HomeCaruselActive, HomeCarusel)
class HomeCaruselActiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'name1', 'name2']
    list_display = ['id', 'name1']
    search_fields = ['id', 'name1', 'name2']

@admin.register(Category, Sub_Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display = ['id', 'name']
    search_fields = ['id', 'name', 'price']

admin.site.register(Panel)
admin.site.register(ProductType)
admin.site.register(HomeLogo)
admin.site.register(Contact)
admin.site.register(Cart)

