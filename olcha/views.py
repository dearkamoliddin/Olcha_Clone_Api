from olcha.models import CategoryModel
from olcha.serializers import CategoryModelSerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

