from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from Main.models import UserProfile, Location, Donation
from Main.forms import UserForm, UserProfileForm, LocationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
# Create your views here.

def __init_dict(u):
    if not u.is_anonymous():
        try:
            current_user_type = UserProfile.objects.get(user = u).user_type
        except UserProfile.DoesNotExist:
            current_user_type = "Super Admin"
        return {'current_user_type': current_user_type}
    return {'current_user_type': "Guest"}

def index(request):
    current_user = request.user
    context_dict = __init_dict(current_user)
    return render(request, 'Main/index.html', context=context_dict)

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index')
            else:
                return HttpResponse('Your account is deasbled.')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Main/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index')

def show_dashboard(request):
    current_user = request.user
    context_dict = __init_dict(current_user)

    locations = Location.objects.all()
    context_dict['locations'] = locations

    if context_dict['current_user_type'] in ['Location Employee', 'Manager', 'Admin']:
        context_dict['can_add_location'] = True
    else:        
        context_dict['can_add_location'] = False

    return render(request, 'Main/dashboard.html', context_dict)

def show_location_detail(request, location_slug):
    context_dict = __init_dict(request.user)
    try:
        location = Location.objects.get(slug = location_slug)
        # donations = Donation.objects.get(location = location)
        context_dict['location'] = location
    except Location.DoesNotExist:
        context_dict['location'] = None
    
    return render(request, 'Main/location.html', context=context_dict)

def add_location(request):
    if request.method == 'POST':
        location_form = LocationForm(data = request.POST)
        if location_form.is_valid():
            location = location_form.save()
            location.save()
            return HttpResponseRedirect('/dashboard')
        else:
            print(location_form.errors)
    else:
        context_dict = __init_dict(request.user)
        context_dict['location_form'] = LocationForm()
        return render(request, 'Main/add_location.html', context = context_dict)


def show_donations(request, location_slug):
    context_dict = __init_dict(request.user)
    try:
        location = Location.objects.get(slug = location_slug)
        # donations = Donation.objects.get(location = location)
        context_dict['location'] = location
    except Location.DoesNotExist:
        context_dict['location'] = None
    
    if context_dict['location']:
        try:
            donations = Donation.objects.filter(location = context_dict['location'])
            context_dict['donations'] = donations
        except Location.DoesNotExist:
            context_dict['donations'] = None
    
    return render(request, 'Main/donations.html', context=context_dict)