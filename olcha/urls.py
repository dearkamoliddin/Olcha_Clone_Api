from django.urls import path
from olcha import views

urlpatterns = [
    # path('category/', views.CategoryListApiView.as_view(), name='category'),
    # path('category/create/', views.CategoryListApiView.as_view(), name='category-create'),
    #
    # path('category/<slug:slug>/detail/', views.CategoryDetailApiView.as_view(), name='category-detail'),
    # path('category/<slug:slug>/edit/', views.CategoryDetailApiView.as_view(), name='category-update'),
    # path('category/<slug:slug>/delete/', views.CategoryDetailApiView.as_view(), name='category-delete'),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/edit/', views.CategoryDetail.as_view()),
]
