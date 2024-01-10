from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import EventModel

class EventSerializer(serializers.ModelSerializer):
    # Image fields
    # image = serializers.ImageField()
    class Meta:
        model = EventModel
        fields = '__all__'