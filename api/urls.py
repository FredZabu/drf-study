from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:pk>', views.ProductDetailAPIView.as_view()),
    path('products/infor', views.product_infor),
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/<str:pk>', views.OrderAPIView.as_view())
]
