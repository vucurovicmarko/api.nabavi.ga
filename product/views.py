from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class CategoryProductList(APIView):
    def get(self, request, category_slug, format=None):
        products = Product.objects.filter(category__slug=category_slug)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)
