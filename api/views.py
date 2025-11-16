from django.db.models import Max
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerializer, productInforSerializer
from api.models import Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(stock__gt = 0)
    serializer_class = ProductSerializer

# @api_view(['GET'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# @api_view(['GET'])
# def order_list(request):
#     orders = Order.objects.prefetch_related('items', 'items__product').all()
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer
    
# @api_view(['GET'])
# def order(request, pk):
#     ordered = get_object_or_404(Order, pk=pk)
#     serializer = OrderSerializer(ordered)
#     return Response(serializer.data)

class OrderAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer
    
@api_view(['GET'])
def product_infor(request):
    product = Product.objects.all()
    serializer = productInforSerializer({
        'product': product,
        'count': len(product),
        'max_price': product.aggregate(max_price = Max('price'))['max_price']
    })
    return Response(serializer.data)