from django.contrib import admin
from olcha.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
