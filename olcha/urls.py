from django.urls import path

from olcha import views

urlpatterns = [
    path('category/', views.CategoryListApiView.as_view(), name='category'),
]
