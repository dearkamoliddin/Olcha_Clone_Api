from django.db.models import Avg
from rest_framework import serializers
from olcha.models import CategoryModel, GroupModel, ProductModel, AttributeModel


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = CategoryModel
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_avg_rating(self, products):
        avg_rating = products.comments.aggregate(avg=Avg('rating'))['avg']
        if not avg_rating:
            return 0
        elif avg_rating > 0:
            return round(avg_rating, 2)

    def get_is_liked(self, products):
        request = self.context.get('request')
        if request.user.is_authenticated:
            if_liked = products.is_liked.filter(id=request.user.id).exists()
            return if_liked
        return False

    def get_image(self, products):
        request = self.context.get('request')
        try:
            image = products.images.get(is_primary=True)
            return request.build_absolute_uri(image.image.url)
        except products.images.model.DoesNotExist:
            return None

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField()

    def get_attributes(self, products):
        attributes = AttributeModel.objects.filter(product=products.id)
        attributes_dict = {}
        for attribute in attributes:
            attributes_dict[attribute.key.name] = attribute.value.name
        return attributes_dict

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'slug', 'attributes']



































# class CategoryModelSerializer(ModelSerializer):
#     group_count = serializers.SerializerMethodField()
#
#     def get_group_count(self, obj):
#         return obj.groups.count()
#
#     class Meta:
#         model = CategoryModel
#         fields = ['id', 'title', 'slug', 'image', 'group_count']
#
#
# class GroupModelSerializer(ModelSerializer):
#     # category = CategoryModelSerializer(read_only=True)
#     category_slug = serializers.SlugField(source='category.slug')
#     category_title = serializers.CharField(source='category.title')
#     full_image_url = serializers.SerializerMethodField(method_name='get_image')
#
#     def get_image(self, obj):
#         image_url = obj.image.url
#         request = self.context.get('request')
#         return request.build_absolute_uri(image_url)
#
#     class Meta:
#         model = GroupModel
#         exclude = ('image',)
#
#
# class ProductModelSerializer(ModelSerializer):
#     category_name = serializers.CharField(source='group.category.title')
#     group_name = serializers.CharField(source='group.title')
#     is_liked = serializers.SerializerMethodField()
#     image = serializers.SerializerMethodField()
#
#     def get_is_liked(self, products):
#         user = self.context['request'].user
#         if user.is_authenticated:
#             if user in products.is_liked.all():
#                 return True
#             return False
#
#     def get_image(self, products):
#         image = products.objects.get(is_prime=True)
#         if image:
#             image_url = image.image.url
#             request = self.context.get('request')
#             return request.build_absolute_uri(image_url)
#
#
#
#     def get_avg_rating(self, products):
#         avg_rating = products.comments.all().aggregate(avg=Round(Avg('rating')))
#         return avg_rating.get('avg', 0)
#
#
#     class Meta:
#         model = ProductModel
#         fields = '__all__'
