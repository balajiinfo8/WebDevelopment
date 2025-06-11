from .models import TODOAPP
from rest_framework import serializers

class TODOAPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOAPP 
        fields = '__all__'