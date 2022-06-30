from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

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


class CategoryDetail(APIView):
    def get(self, request, category_slug, format=None):
        category = get_object_or_404(Category, slug=category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    print(request)
    
    query = request.data.get('q', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    else:
        return Response({"products": []})
