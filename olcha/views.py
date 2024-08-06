# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from olcha.serializers import CategoryModelSerializer
# from olcha.models import CategoryModel

from olcha.models import CategoryModel
from olcha.serializers import CategoryModelSerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


# class CategoryListApiView(APIView):
#     def get(self, request):
#         categories = CategoryModel.objects.all()
#         serializer = CategoryModelSerializer(categories, many=True)
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
# class CategoryDetailApiView(APIView):
#     def get(self, request, slug):
#         category = CategoryModel.objects.get(slug=slug)
#         serializer = CategoryModelSerializer(category)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, slug):
#         category = CategoryModel.objects.get(slug=slug)
#         serializer = CategoryModelSerializer(data=request.data, instance=category)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'message': 'Category successfully updated!',
#                 'status': status.HTTP_200_OK,
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, slug):
#         category = CategoryModel.objects.get(slug=slug)
#         if category:
#             category.delete()
#             data = {
#                 'message': 'Category successfully deleted!',
#                 'status': status.HTTP_200_OK,
#             }
#             return Response(data)


