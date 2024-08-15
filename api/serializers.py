from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.Serializer):
    class Meta:
        model = Data
        fields = '__all__'