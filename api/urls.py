from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>', views.product_detail),
    path('products/infor', views.product_infor),
    path('orders/', views.order_list),
    path('orders/<str:pk>', views.order)
]
