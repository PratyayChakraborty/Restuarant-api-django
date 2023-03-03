from django.contrib import admin
from django.urls import include, path
from apis.views import RestaurantViewSet
from rest_framework import routers

router =routers.DefaultRouter();
router.register(r'restaurants',RestaurantViewSet)

urlpatterns = [
    path('',include(router.urls)),
]