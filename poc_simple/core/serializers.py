from rest_framework import serializers

from core import models


class ToolSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tool
        fields = '__all__'
