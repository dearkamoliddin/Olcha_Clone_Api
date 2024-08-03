from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import CategoryModel


class CategoryListApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category_data = [
            {
                'title': category.title,
                'slug': category.slug,
                'image': category.image.url,
            }
            for category in CategoryModel.objects.all()]
        return Response(data=category_data, status=status.HTTP_200_OK)
