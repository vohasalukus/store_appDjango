from django.urls import path
from .views import (main, add_store, delete_store, edit_store, category, add_category,
                    delete_category, edit_category, products, add_product, delete_product, edit_product)

urlpatterns = [
    path('', main, name='main'),
    path('add_store/', add_store, name='add_store'),
    path('delete_store/<slug:slug>', delete_store, name='delete_store'),
    path('edit_store/<slug:slug>', edit_store, name='edit_store'),
    path('category/', category, name='category'),
    path('category/add_category/', add_category, name='add_category'),
    path('delete_category/<slug:slug>', delete_category, name='delete_category'),
    path('category/edit_category/<slug:slug>', edit_category, name='edit_category'),
    path('category/products/<slug:slug>', products, name='products'),
    path('category/products/add_product/', add_product, name='add_product'),
    path('category/products/delete_product/<slug:slug>', delete_product, name='delete_product'),
    path('category/products/edit_product/<slug:slug>', edit_product, name='edit_product'),

]
