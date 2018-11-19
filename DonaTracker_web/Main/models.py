from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import uuid

#user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length = 60, default = "Regular User")

    def __str__(self):
        return self.user.username

#Location and donation
class Location(models.Model):
    uuid = models.UUIDField(primary_key=True, 
        default=uuid.uuid4, 
        editable = False)
    name = models.CharField(max_length = 128, default = "name undefined")
    type = models.CharField(max_length = 64, default = "default type")
    
