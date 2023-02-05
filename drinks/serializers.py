# Python object -> Json serializer
from rest_framework import serializers

from drinks.models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    # Metadata
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']