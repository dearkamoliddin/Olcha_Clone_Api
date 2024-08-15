from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from olcha.models import ProductModel
from rest_framework.views import APIView
from rest_framework.response import Response
from olcha.serializers import ProductSerializer, ProductDetailSerializer, AttributeSerializer


class ProductList(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, category_slug, group_slug):
        products = ProductModel.objects.filter(group__category__slug=category_slug, group__slug=group_slug)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get(self, request, category_slug, group_slug, product_slug):
        product = get_object_or_404(ProductModel, slug=product_slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug, group_slug, product_slug):
        product = ProductModel.objects.get(slug=product_slug)
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug, group_slug, product_slug):
        product = ProductModel.objects.get(slug=product_slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsAttribute(APIView):
    def get(self, request, category_slug, group_slug):
        products = ProductModel.objects.filter(group__category__slug=category_slug, group__slug=group_slug)
        serializer = AttributeSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAttribute(APIView):

    def get(self, request, category_slug, group_slug, product_slug):
        product = ProductModel.objects.get(slug=product_slug)
        serializer = AttributeSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug, group_slug, product_slug):
        product = ProductModel.objects.get(slug=product_slug)
        serializer = AttributeSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug, group_slug, product_slug):
        product = ProductModel.objects.get(slug=product_slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
