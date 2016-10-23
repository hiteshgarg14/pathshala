from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, StandardForm, EditUserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile, Standard

def home(request):
    return render(request, 'school/index.html',{})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        std_form = StandardForm(request.POST)
        profile_form = EditUserProfileForm(request.POST)
        if form.is_valid() and std_form.is_valid() and profile_form.is_valid():
            user = form.save()
            password = user.password
            # hash the password
            user.set_password(user.password)
            user.save()
            user2 = profile_form.save(commit=False)
            user2.profileuser = user
            user2.save()
            #user4 = std_form.save(commit=False)
            #user4.user = user
            new_data = []
            sub_names = request.POST.get('sub_names')
            ss = sub_names.strip().split(",")
            for x in range(0,len(ss)):
                new_data.append(Standard(user=user,std=request.POST.get('std'),sub_name=ss[x]))
            Standard.objects.filter(user=user).delete()
            Standard.objects.bulk_create(new_data)
            #user4.save()
            user3 = authenticate(username=user.username, password=password)
            if user3:
                if user3.is_active:
                    login(request, user3)
                    return redirect('school:profle_user',user_id=request.user.id)
                else:
                    return HttpResponse("Your account is disabled.")
            return HttpResponse("registered")
        else:
            print form.errors
            return render(request,'school/login_user.html', {'form': form, 'std_form':std_form,'profile_form':profile_form})
    else:
        form = UserForm()
        std_form = StandardForm()
        profile_form = EditUserProfileForm()
        print std_form
    return render(request,'school/login_user.html', {'form': form, 'std_form':std_form,'profile_form':profile_form})

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
                return redirect('school:profle_user',user_id=request.user.id)
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid Login details: {0},{1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'school/login_user.html', {})

@login_required
def profile_user(request,user_id):
    userprofile = get_object_or_404(UserProfile,profileuser=request.user)
    stdprofile = Standard.objects.filter(user=request.user)
    for stdr in stdprofile:
        st = stdr.std
    return render(request, 'school/profile.html',{'userprofile':userprofile,'stdprofile':stdprofile,'st':st})

@login_required
def search_student(request):
    subject = request.GET.get('q')
    subject = str(subject)
    data = Standard.objects.filter(sub_name=subject)
    users = []
    for d in data:
        for dd in User.objects.filter(username=d):
            users.append(dd)
    return render(request, 'school/searchresults.html',{'users':users})

"""
@login_required
def edit_user_profile(request, user_id):
    puser = get_object_or_404(UserProfile, profileuser= request.user)
    std_user = get_object_or_404(Standard, user= request.user)
    ext_user = get_object_or_404(InterstedSubject, std=request.user.std)
    if request.method == 'POST':
        std_form =StandardForm(data=request.POST,instance=std_user)
        profile_form = UserProfileForm(data=request.POST, instance=puser)
        ext_form = UserEditForm(data=request.POST, instance=request.user.std)
        if std_form.is_valid() and profile_form.is_valid() and ext_form.is_valid():
    	    profile = profile_form.save(commit=False)
    	    profile.profileuser = request.user
    		if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile_form.save()
            std_form.save()
            ext_form.save()
            pass
    else:
        std_form =StandardForm(instance=std_user)
    	profile_form = UserProfileForm(instance=puser)
    	ext_form = UserEditForm(instance=request.user.std)
    return  render(request,'fosssite/edit_user_profile.html',{'profile_form':profile_form, 'std_form':std_form, 'ext_form':ext_form})
"""

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def public_profile(request,user_id):
    user = get_object_or_404(User,profileuser=user_id)
    userprofile = get_object_or_404(UserProfile,profileuser=user_id)
    stdprofile = Standard.objects.filter(user=user_id)
    for stdr in stdprofile:
        st = stdr.std
    return render(request, 'school/public_profile.html',{'sub_name':sub_name,'userprofile':userprofile,'stdprofile':stdprofile,'st':st,'user':user})
