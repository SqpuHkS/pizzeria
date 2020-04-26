from .views import *
from django.urls import path

urlpatterns = [
    path('order_create/', order_create, name="order_create"),
    path('create/', CreateIngredient.as_view(), name="create-page"),
    path('delete/<str:name>', ingredient_delete, name="delete-page"),
    path('edit/<str:name>', EditIngredient.as_view() ,name="edit-page"),
    path('', index, name="main-page"),
]
