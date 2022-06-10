from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', views.restaurant_list),
    path('restaurants/<str:pk>/reviews', views.createRestaurantReview),
    path('restaurants/<str:pk>', views.restaurant_detail),
    path('api/', include('base.user_api.urls'))
]

