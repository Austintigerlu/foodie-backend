from django.urls import path 
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/register/', views.registerUser, name='register')
]