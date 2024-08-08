from django.urls import path
from olcha.views.category.views import CategoryListApiView, CategoryDetail
from olcha.views.group.views import GroupCreateApiView, GroupListAPIView, GroupDetailApiView
from olcha.views.product.views import ProductListApiView

urlpatterns = [
    path('category/', CategoryListApiView.as_view(), name='category-list'),
    path('category/<slug:slug>/edit/', CategoryDetail.as_view(), name='category-detail'),

    path('group/create/', GroupCreateApiView.as_view(), name='group-create'),
    path('category/<slug:slug>/', GroupListAPIView.as_view(), name='group-list'),
    path('group/<slug:slug>/detail/', GroupDetailApiView.as_view(), name='group-detail'),

    path('category/<slug:category_slug>/<slug:group_slug>/', ProductListApiView.as_view(), name='product-list'),
]
