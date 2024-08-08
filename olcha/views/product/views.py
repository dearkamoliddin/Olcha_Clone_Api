from rest_framework.generics import ListAPIView

from olcha.models import ProductModel
from olcha.serializers import ProductModelSerializer


class ProductListApiView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        group_slug = self.kwargs['group_slug']
        queryset = ProductModel.objects.filter(group__category__slug=category_slug, group__slug=group_slug)
        return queryset
