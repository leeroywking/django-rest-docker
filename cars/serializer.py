from rest_framework import serializers
from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("make", "model", "style", "name", "country_of_origin")
        model = Cars
