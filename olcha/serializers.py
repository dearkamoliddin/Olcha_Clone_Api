from django.db.models import Avg
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token

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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, required=True)

    class Meta:
        fields = ['username', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, username):
        username = self.validated_data['username']
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {
                    'data': f'{username} already exists',
                }
            )
        return username

    def validate(self, instance):
        if instance['password'] != instance['password2']:
            data = {
                'error': 'Passwords do not match',
            }
            raise serializers.ValidationError(detail=data)

        if User.objects.filter(email=instance['email']).exists():
            raise serializers.ValidationError({"message": "Email already taken!"})

        return instance

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
