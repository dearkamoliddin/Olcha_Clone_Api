from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import CategoryModel
from olcha.serializers import CategoryModelSerializer
from rest_framework import generics, status


class CategoryListApiView(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategoryModelSerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Category successfully created!', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


