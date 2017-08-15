from django.shortcuts import render_to_response, redirect, HttpResponse, render, HttpResponseRedirect, reverse
from .forms import UserCreationForm, LoginForm, SubscriptionsForm, UpdateProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Subscriptions
from django.template import RequestContext
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.db.models import Q
from django.contrib.auth import views as auth_views
from django.utils.timezone import now
from .Decorator import login_required
import json



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            sub = form.cleaned_data.get('sub')
            rule = form.cleaned_data.get('rule')
            if password != password2:
                messages.error(request, 'پسورد هم خوانی ندارد!!!')
            elif rule is False:
                messages.error(request, 'قوانین را مطالعه کنید!!!')
            else:
                user = form.save()
                user.set_password(user.password)
                user.save()
                users = authenticate(email=email, password=password)
                login(request, users)
                if sub is True:
                    sub = Subscriptions(sub_email=email)
                    sub.save()
                    # sub_form = SubscriptionsForm(request.POST)
                    # SubscriptionsForm.sub_email = data['email']
                    # sub_form.save()
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# def user_login(request):
#     form = LoginForm(request.POST or None)
#     if request.POST and form.is_valid():
#         user = form.login(request)
#         if user:
#             login(request, user)
#             return HttpResponseRedirect("/")# Redirect to a success page.
#     return render(request, 'login.html', {'form': form })


def user_login(request):

    if request.method == 'POST':
          email = request.POST['email']
          password = request.POST['password']
          user = authenticate(email=email, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  return HttpResponseRedirect("/")
              else:

                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              form = LoginForm(request.POST)
              return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'login.html', {'form': form})



def subscription(request):
    if request.method == 'POST' and 'sub_email' in request.POST:
        form = SubscriptionsForm(request.POST)
        if form.is_valid():
            sub_email = form.cleaned_data.get('email')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'یه چیزی اشتباه!!!')
    else:
        form = SubscriptionsForm(request.POST)
    return render(request, 'base.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect(reverse('home'))
    # return HttpResponse(json, mimetype='application/json')
    return render(request, 'base.html',)


def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse("ok shd.")
        else:
            return HttpResponse("nashod.")
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'profile.html', args)