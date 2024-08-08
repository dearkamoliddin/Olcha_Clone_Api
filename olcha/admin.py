from django.contrib import admin
from olcha.models import CategoryModel, GroupModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
