from django.urls import path 
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', views.registerUser, name='register')
]