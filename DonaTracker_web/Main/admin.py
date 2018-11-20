from django.contrib import admin
from Main.models import UserProfile, Location
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'type',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Location, LocationAdmin)