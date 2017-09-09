from django.db import models

from user.models import User

# Create your models here.


class Event(models.Model):
    EVENT_TYPE = (('Yearly', 'Birthday'),
                  ('Yearly', 'Anniversary'),
                  ('Monthly', 'Monthly Bill'),
                  ('Onetime',  'One time event'),
                  ('Daily',   'Daily'),
                 )

    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Name of the event")
    description = models.TextField()
    event_type = models.CharField(max_length=255, choices=EVENT_TYPE)
    day = models.PositiveIntegerField(help_text="Day of the event", default=0)
    month = models.PositiveIntegerField(default=0, help_text="Month of the\
                                       event")
    year = models.PositiveIntegerField(default=0, help_text="Year of the\
                                        event")
    hour = models.PositiveIntegerField(default=0, help_text="Hour of the\
                                       event")
    minute = models.PositiveIntegerField(default=0, help_text="Minute of the\
                                         event")
    frequency = models.PositiveIntegerField(default=1, help_text="Interval for\
                                           notifications in hours")
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "events"

    def __str__(self):
        return self.name

