from rest_framework import serializers

from apis.models import Restaurant
#Restaurant serializer
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields="__all__"