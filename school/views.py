from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .froms import UserForm
from django.contrib.auth.models import User

def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = form.save()
            # hash the password
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print form.errors
    else:
        form = UserForm()
    return render(request,'school/register.html', {'form': form, 'registered': registered})
