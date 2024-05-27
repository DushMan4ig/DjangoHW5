# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
]
