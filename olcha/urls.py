from django.urls import path
from olcha import views

urlpatterns = [
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/edit/', views.CategoryDetail.as_view(), name='category-detail'),
]
