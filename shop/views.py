from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'shop/order_list.html', {'orders': orders})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'shop/order_detail.html', {'order': order})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
