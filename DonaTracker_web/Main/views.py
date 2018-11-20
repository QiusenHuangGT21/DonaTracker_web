from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from Main.models import UserProfile
from Main.forms import UserForm, UserProfileForm

# Create your views here.
from django.http import HttpResponse 

def index(request):
    return render(request, 'Main/index.html', context=None)

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {'user_form': user_form, 'profile_form': profile_form
        , "registered": registered, }

    return render(request, 'Main/registration.html', context=context_dict)
