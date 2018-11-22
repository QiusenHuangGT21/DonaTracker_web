from django.contrib import admin
from Main.models import UserProfile, Location, Donation
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'type', 'lat', 'lng')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'short_description', 'value', 'location', 'category')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Donation, DonationAdmin)