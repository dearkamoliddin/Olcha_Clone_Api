from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from olcha.models import CategoryModel, GroupModel, ProductModel


class CategoryModelSerializer(ModelSerializer):
    group_count = serializers.SerializerMethodField()

    def get_group_count(self, obj):
        return obj.groups.count()

    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'slug', 'image', 'group_count']


class GroupModelSerializer(ModelSerializer):
    # category = CategoryModelSerializer(read_only=True)
    category_slug = serializers.SlugField(source='category.slug')
    category_title = serializers.CharField(source='category.title')
    full_image_url = serializers.SerializerMethodField(method_name='get_image')

    def get_image(self, obj):
        image_url = obj.image.url
        request = self.context.get('request')
        return request.build_absolute_uri(image_url)

    class Meta:
        model = GroupModel
        exclude = ('image',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
