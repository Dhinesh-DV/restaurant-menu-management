from django.contrib import admin
from .models import Chef, Category, MenuItem, DiningTable


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'chef', 'price', 'is_available']
    search_fields = ['name', 'chef__name']
    list_filter = ['category', 'is_available', 'chef']
    readonly_fields = ['created_at']


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity']
    search_fields = ['table_number']


