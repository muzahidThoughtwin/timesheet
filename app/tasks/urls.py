from django.conf.urls import url
from app.tasks import views
app_name='tasks'

urlpatterns = [
	# url(r'^task/edittask$',views.EditTask.as_view()),
	# url(r'^task/edittask/(?P<user_id>[0-9]+)$',views.EditTask.as_view()),
	url(r'^task/calculate_hours/(?P<user_id>[0-9]+)$',views.CalculateHrs.as_view()),
	url(r'^task/taskdetail/(?P<user_id>[0-9]+)$',views.UserTaskDatewise.as_view()),
	url(r'^task/list$',views.GetTask.as_view()),
	url(r'^task/list/(?P<task_id>[0-9]+)$',views.GetUsersTasks.as_view()),
	url(r'^task',views.TaskView.as_view()),
]
