from django.contrib import admin
from .models import Restaurant, Meal, Category


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'created']
    list_filter = ['created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'image', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
