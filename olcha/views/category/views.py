from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from olcha.models import CategoryModel
from olcha.serializers import CategorySerializer


class CategoryList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, category_slug):
        try:
            category = CategoryModel.objects.get(slug=category_slug)
        except CategoryModel.DoesNotExist:
            raise Http404

        serializer = CategorySerializer(category)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug):
        category = CategoryModel.objects.get(slug=category_slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from olcha.models import CategoryModel
# from olcha.serializers import CategoryModelSerializer
# from rest_framework import generics, status
#
#
# class CategoryListApiView(APIView):
#     def get(self, request):
#         categories = CategoryModel.objects.all()
#         serializer = CategoryModelSerializer(categories, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CategoryModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Category successfully created!', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CategoryModel.objects.all()
#     serializer_class = CategoryModelSerializer
#
#
