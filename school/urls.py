from django.conf.urls import url
from . import views

app_name = 'school'
urlpatterns = [
	url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
	
]
