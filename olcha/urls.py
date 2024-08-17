from django.urls import path
from olcha.views.auth.views import LoginAPIView, LogoutAPIView, RegisterAPIView
from olcha.views.category.views import CategoryList, CategoryDetail
from olcha.views.group.views import GroupList, GroupDetail
from olcha.views.product.views import (
    ProductList,
    ProductDetail,
    ProductAttribute,
    ProductCreateAPIView,
    ProductDetailAPIView
)


urlpatterns = [
    # category
    path('category/', CategoryList.as_view()),
    path('category/detail/<slug:category_slug>/', CategoryDetail.as_view()),

    # group
    path('category/<slug:category_slug>/', GroupList.as_view()),
    path('category/<slug:category_slug>/<slug:group_slug>/detail/', GroupDetail.as_view()),

    # product
    path('product-list/', ProductCreateAPIView.as_view(),),
    path('product-list/<int:pk>/', ProductDetailAPIView.as_view(),),

    path('category/<slug:category_slug>/<slug:group_slug>/', ProductList.as_view()),
    path('category/<slug:category_slug>/<slug:group_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('category/<slug:category_slug>/<slug:group_slug>/<slug:product_slug>/attribute/', ProductAttribute.as_view()),

    # Login View
    path("login/", LoginAPIView.as_view(), name="user_login"),
    path("register/", RegisterAPIView().as_view(), name="user_register"),
    path("logout/", LogoutAPIView.as_view(), name="user_logout")
]
