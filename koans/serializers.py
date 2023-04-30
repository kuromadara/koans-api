from rest_framework import serializers
from .models import Koan

class KoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Koan
        fields = '__all__'