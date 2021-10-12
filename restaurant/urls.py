from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('create/', views.restaurant_create, name='create'),
    path('view/', views.restaurant_list, name='view'),
    # path('like/', views.image_like, name='like'),
    path('view/<name>/', views.restaurant_detail, name='restaurant_detail'),
    path('categories/', views.restaurant_meal_categories, name='restaurant_meal_categories'),
    path('order/', views.meal_list, name='meal_list'),
    path('<slug:category_slug>/', views.meal_list, name='meal_list_by_category'),
    path('<int:id>/<slug:slug>/', views.meal_detail, name='meal_detail'),
    
]
