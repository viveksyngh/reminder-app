from django.shortcuts import render

from rest_framework import viewsets

from . import serializers
from . import models 

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()

