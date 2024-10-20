from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api.public.views import *


app_name = 'users_public'

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns += router.urls
