from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import UserViewSet, PaymentViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='UserViewSet')
router_v1.register('payments', PaymentViewSet, basename='PaymentViewSet')

urlpatterns = [
    re_path('', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]