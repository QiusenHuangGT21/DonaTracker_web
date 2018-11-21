from django.db import models
from django.contrib.auth.models import User
import uuid

#user
class UserProfile(models.Model):
    REGULAR_USER = 'User'
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
    name = models.CharField(max_length = 128, default = "(name)")
    lat = models.DecimalField(max_digits= 20, decimal_places=17, default = 0.0)
    lng = models.DecimalField(max_digits= 20, decimal_places=17, default = 0.0)
    street = models.CharField(max_length = 128, default = "(street)")
    address = models.CharField(max_length = 128, default = "(address")
    city = models.CharField(max_length = 20, default = "(city)")
    State = models.CharField(max_length = 10, default = "(state)")
    zip = models.IntegerField(default=99999)
    type = models.CharField(max_length = 64, default = "default type")
    phone = models.IntegerField(default=0)
    website = models.CharField(max_length = 128, default = "(website)")
    employees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Donation(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    date = models.DateField(auto_now_add=True, editable = False)
    location = models.ForeignKey(Location)
    short_description = models.CharField(max_length = 20, default = "short description")
    full_description = models.CharField(max_length = 256, default = "full description")
    value = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.CharField(max_length = 128, default = "default")
    
    def __str__(self):
        return self.short_description

