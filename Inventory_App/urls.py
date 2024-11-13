from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_create, name='category-list-create'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('orders/', views.order_list_create, name='order-list-create'),
    path('orders/<int:pk>/', views.order_details, name='order-detail'),
]
