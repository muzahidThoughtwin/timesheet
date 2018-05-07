from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects
from datetime import datetime


class Tasks(models.Model):
	project = models.ForeignKey(Projects)
	user = models.ForeignKey(User)
	date = models.DateField(default=datetime.now)
	hours = models.TimeField(auto_now_add=False, blank=True)
	description = models.CharField(max_length=1000,default='Description Not Provided')
	is_billing = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


	# def get_list(self):
	# 	if self.project:
	# 		return self.project.split(',')