from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = models.Product.objects.all()[0:4]
        serializer = serializers.ProductSerializer(products, many=True)

        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = [category.name for category in models.Category.objects.all()]

        return Response(categories)
