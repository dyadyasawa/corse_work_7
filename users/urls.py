
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # path("payment/", PaymentsListApiView.as_view(), name="payment_list"),
    # path("payment_create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    # path("payment/detail/<int:pk>/", PaymentsRetrieveApiView.as_view(), name="payment_detail"),
    # path("payment/create/", PaymentsCreateApiView.as_view(), name="payment_create"),
    # path("payment/update/<int:pk>/", PaymentsUpdateApiView.as_view(), name="payment_update"),
    # path("payment/delete/<int:pk>/", PaymentsDestroyApiView.as_view(), name="payment_delete"),

    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]
