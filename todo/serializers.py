from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.serializers import ModelSerializer

class PlanSerializer(ModelSerializer):
    class Meta:
        model=Plan
        fields= '__all__'