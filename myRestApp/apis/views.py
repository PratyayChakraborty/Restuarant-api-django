from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from apis.models import Restaurant
from apis.serializers import RestaurantSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['Restaurant_id','Cost','cuisineTypes','isOpen','vegOnly']
    search_fields = ['Restaurant_id','Cost','cuisineTypes','Address','name']
    ordering_fields = ['Restaurant_id','Cost','cuisineTypes','Address','name']