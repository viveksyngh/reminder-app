from rest_framework import serializers

from . import models

class EventSerializer(serializers.ModelSerializer):
    
    # user = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = models.Event
        fields = ('event_id', 'name', 'description', 'frequency', 'event_type', 'day',
                  'month', 'year', 'hour', 'minute', 'created_on', 'user')
        
