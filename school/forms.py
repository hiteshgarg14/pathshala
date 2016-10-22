from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, InterstedSubjects


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password']
