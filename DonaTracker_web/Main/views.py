from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from Main.models import UserProfile, Location, Donation
from Main.forms import UserForm, UserProfileForm, LocationForm, DonationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
from django.db.models import Q
# import uuid
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
    if context_dict['current_user_type'] in ['Location Employee', 'Manager', 'Admin']:
        context_dict['can_add_donation'] = True
    else:        
        context_dict['can_add_donation'] = False
    return render(request, 'Main/donations.html', context=context_dict)

def add_donation(request, location_slug):
    if request.method == 'POST':
        donation_form = DonationForm(data = request.POST)
        if donation_form.is_valid():
            donation = donation_form.save()
            donation.location = Location.objects.get(slug = location_slug)
            donation.save()
            return HttpResponseRedirect('/dashboard')
        else:
            print(donation_form.errors)
    else:
        context_dict = __init_dict(request.user)
        context_dict['location'] = Location.objects.get(slug = location_slug)
        context_dict['donation_form'] = DonationForm()
        return render(request, 'Main/add_donation.html', context = context_dict)


def search_display(request):
    if request.method == 'GET':
        return render(request, 'Main/search_display.html', context = {})


def search_all_Location(request):
    if request.method == 'POST':
        error_msg = ''
        name = request.POST.get('name')
        donations = Donation.objects.filter(short_description = name)
        return render(request, 'Main/search_Location_res.html', {'donations':donations})
    else:
        error_msg = 'Not POST method'
        return render(request, 'Main/search_error.html')


def search_Donation(request):
    if request.method == 'POST':
        error_msg = ''
        location_uuid = request.POST.get('location')
        print(location_uuid)
        name = request.POST.get('name')
        location = Location.objects.get(uuid = location_uuid)
        all_donations = Donation.objects.filter(location = location)
        real_donation_list = []
        for donation in all_donations:
            if donation.short_description == name:
                real_donation_list.append(donation)
        # print(donations)
        return render(request, 'Main/search_Location_res.html', {'donations':real_donation_list})
    else:
        return render(request, 'Main/search_error.html')



def search_Donation_by_category(request):
    if request.method == 'POST':
        error_msg = ''
        name = request.POST.get('category')
        donations = Donation.objects.filter(category = name)
        return render(request, 'Main/search_Donation_by_cat_result.html', {'donations':donations})
    else:
        error_msg = 'Not POST method'
        return render(request, 'Main/search_error.html')































