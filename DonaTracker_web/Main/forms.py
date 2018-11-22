from django import forms
from django.contrib.auth.models import User
from Main.models import UserProfile, Location, Donation

class UserForm(forms.ModelForm):
    password = forms.CharField(required = True, widget=forms.PasswordInput())
    username = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_type',)

class LocationForm(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = ("name","street_address","city","state",'zip','type', 'phone', "website")
    



