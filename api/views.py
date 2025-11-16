from django.db.models import Max
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerializer, productInforSerializer
from api.models import Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related('items', 'items__product').all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order(request, pk):
    ordered = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(ordered)
    return Response(serializer.data)

@api_view(['GET'])
def product_infor(request):
    product = Product.objects.all()
    serializer = productInforSerializer({
        'product': product,
        'count': len(product),
        'max_price': product.aggregate(max_price = Max('price'))['max_price']
    })
    return Response(serializer.data)