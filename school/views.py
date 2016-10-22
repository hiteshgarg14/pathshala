from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'school/index.html',{})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        step2_form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            # hash the password
            user.set_password(user.password)
            user.save()
            user2 = step2_form.save(commit=False)
            user2.profileuser = user
            user2.save()
            return HttpResponse("registered")
        else:
            print form.errors
            print step2_form.errors
            return render(request,'school/login_user.html', {'form': form, 'step2_form':step2_form})
    else:
        form = UserForm()
        step2_form = UserProfileForm()
    return render(request,'school/login_user.html', {'form': form, 'step2_form':step2_form})

"""
def register_step2(request):
    if request.method == 'POST':
        step2_form = UserProfileForm(request.POST)
        if step2_form.is_valid():
            user = step2_form.save(commit=False)
            user.profileuser = request.user
            user.save()
            return HttpResponse("registered")
        else:
            print step2_form.errors
            return render(request,'school/register_step2.html',{'step2_form':step2_form})
    else:
        step2_form = UserProfileForm()
        print step2_form
    return render(request, 'school/register_step2.html',{'step2_form':step2_form})
"""

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #Django method called reverse to obtain the URL of the Rango application.
                return HttpResponse("login")
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid Login details: {0},{1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'school/login_user.html', {})
