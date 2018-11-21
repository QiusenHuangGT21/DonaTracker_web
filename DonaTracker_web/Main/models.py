from django.db import models
from django.contrib.auth.models import User
import uuid

#user
class UserProfile(models.Model):
    REGULAR_USER = 'Uset'
    LOCATION_EMPLOYEE = 'Location Employee'
    MANAGER = 'Manager'
    ADMIN = 'Admin'
    USER_TYPE_CHOICES = (
        (REGULAR_USER, 'Regular User'),
        (LOCATION_EMPLOYEE, 'Location Employee'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length = 1, 
        choices = USER_TYPE_CHOICES,
        default = REGULAR_USER,)

    def __str__(self):
        return self.user.username

#Location and donation
class Location(models.Model):
    uuid = models.UUIDField(primary_key=True, 
        default=uuid.uuid4, 
        editable = False)
    name = models.CharField(max_length = 128, default = "name undefined")
    type = models.CharField(max_length = 64, default = "default type")
    
