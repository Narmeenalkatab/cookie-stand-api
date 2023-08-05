from rest_framework import serializers
from .models import flowers


class flowerserializer(serializers.ModelSerializer):
    class Meta:
        model = flowers
        fields = "__all__"
