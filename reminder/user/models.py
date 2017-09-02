from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    secondary_email = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

