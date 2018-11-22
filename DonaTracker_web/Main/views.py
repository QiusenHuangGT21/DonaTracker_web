from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from Main.models import UserProfile
from Main.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse 

def index(request):
    current_user = request.user
    context_dict = {}
    if not current_user.is_anonymous():
        try:
            current_user_type = UserProfile.objects.get(user = current_user).user_type
        except UserProfile.DoesNotExist:
            current_user_type = "Super Admin"
        context_dict = {'current_user_type': current_user_type}
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
    