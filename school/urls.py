from django.conf.urls import url
from . import views

app_name = 'school'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
	#url(r'^register_step2/$', views.register_step2, name='register_step2'),
    url(r'^login_user/$', views.login_user, name='login_user'),

]
