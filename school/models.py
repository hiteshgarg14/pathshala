from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profileuser = models.OneToOneField(User)
    phone_no = models.CharField(blank=False,max_length=15)
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150)
    city = models.CharField(blank=False,max_length=20)
    state = models.CharField(blank=False,max_length=20)
    country = models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.profileuser.username

class InterstedSubjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    std = models.CharField(max_length=20)


    def __str__(self):
        return self.user
