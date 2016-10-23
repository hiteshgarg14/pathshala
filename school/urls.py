from django.conf.urls import url
from . import views

app_name = 'school'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
	#url(r'^register_step2/$', views.register_step2, name='register_step2'),
    url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^(?P<user_id>[0-9]+)/profile_user/$', views.profile_user, name='profle_user'),
	url(r'^(?P<user_id>[0-9]+)/public_user/$', views.public_profile, name='public_user'),
	#url(r'^(?P<user_id>[0-9]+)/edit_user_profile/$', views.edit_user_profile, name='edit_user_profile'),
	url(r'^search_student/$', views.search_student, name='search_student'),

]
