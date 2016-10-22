from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User

def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # hash the password
            user.set_password(user.password)
            user.save()
            return HttpResponse("registered")
        else:
            print form.errors
            return render(request,'school/login_user.html', {'form': form})
    else:
        form = UserForm()
        print form
    return render(request,'school/login_user.html', {'form': form})

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
