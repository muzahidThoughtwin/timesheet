from django.conf.urls import url
from . import views
# import django_twilio

app_name='users'

urlpatterns = [
	url(r'^user/login$',views.Login.as_view(),name='login'),
	url(r'^user/dashboard$',views.Dashboard.as_view()),
	url(r'^user/assignedprojects$', views.UserAssignedProject.as_view()),
	url(r'^user/editprofile$',views.UserDetail.as_view()),
	url(r'^admin/dashboard$',views.AdminDashboard.as_view()),
	url(r'^admin/editprofile$',views.EditAdminDetails.as_view()),
	url(r'^admin/adduser$',views.AddUser.as_view()),
	url(r'^admin/assignproject$',views.AssignProjectTemplate.as_view()),
	url(r'^admin/assignprojectdetails$',views.AssignProjectApi.as_view()),
	url(r'^admin/getassignedproject$',views.GetAssignProject.as_view()),
	url(r'^admin/alluserstasks$',views.AllWorkDetails.as_view()),
	url(r'^admin/tasks$',views.WorkDetailsTemplate.as_view()),
	url(r'^admin/taskslist$',views.WorkDetails.as_view()),
	url(r'^admin/addproject$',views.AddProject.as_view()),
	url(r'^admin/viewuserprojects$',views.ViewProjectApi.as_view()),
	url(r'^admin/viewprojects$',views.ViewProjectTemplate.as_view()),
	# url(r'^login/(?P<user_id>[0-9]+)$',views.Login.as_view()),
	url(r'^user/(?P<user_id>[0-9]+)$',views.UserProfileList.as_view()),
	url(r'^user/tasks$',views.UserTaskDetails.as_view()),
	url(r'^admin/deleteuser$',views.DeleteUser.as_view()),
	url(r'^sendmail/(?P<user_id>[0-9]+)$',views.SendMail.as_view()),
	url(r'^sendsms$',views.SendSmsTemplate.as_view()),
	# url(r'',views.UserProfileList.as_view()),

	# url(r'^api/$', views.home),
	# url(r'^send/', views.sms),
]