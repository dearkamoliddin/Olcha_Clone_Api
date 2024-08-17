
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken import views
from root import custom_token
from root.custom_obtain_views import CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('olcha/', include('olcha.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', custom_token.CustomTokenObtain.as_view()),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/token/blacklist/', TokenBlacklistView.as_view()),
    path('api-logout/', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
