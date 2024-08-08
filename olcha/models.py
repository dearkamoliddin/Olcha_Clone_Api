from typing import Any
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    objects = models.Manager

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(CategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class GroupModel(BaseModel):
    title = models.CharField(max_length=90, unique=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='media/images/group/')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='groups')

    objects = models.Manager

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(GroupModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class ProductModel(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='products')
    is_liked = models.ManyToManyField(User, related_name='liked_products', blank=True)

    objects = models.Manager

    @property
    def discounted_price(self) -> Any:
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100.0))
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ImageModel(BaseModel):
    image = models.ImageField(upload_to='media/images/products/')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class CommentModel(BaseModel):
    class Rating(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    message = models.TextField()
    rating = models.IntegerField(choices=Rating.choices, default=Rating.One.value)
    file = models.FileField(upload_to='comments/')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    objects = models.Manager


class Key(BaseModel):
    name = models.CharField(max_length=70)


class Value(BaseModel):
    name = models.CharField(max_length=250)


class Attribute(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    objects = models.Manager
