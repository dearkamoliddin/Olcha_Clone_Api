from django.contrib import admin
from olcha.models import ProductModel, CategoryModel, GroupModel, CommentModel, ImageModel, AttributeModel, Key, Value


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'slug')


@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'slug', 'created_at')


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'price', 'discount', 'created_at')


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'rating', 'created_at')


admin.site.register(ImageModel)
admin.site.register(Key)
admin.site.register(Value)
admin.site.register(AttributeModel)
