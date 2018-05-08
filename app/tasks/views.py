# from django.contrib.auth import authenticate
# from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from app.tasks.models import Tasks
from django.shortcuts import render,redirect
from app.projects.serializers import ProjectSerializer
from app.projects.models import Projects
from app.users.models import UserProfile
from datetime import datetime, timedelta


## written by aarti
class TaskView(APIView):


	# def post(self,request,**kwargs):
	# 	try:
	# 		print(request.data)
	# 		if "data" in kwargs:
 	#        	data = kwargs["data"]
 	#        	if isinstance(data, list):
 	#            	kwargs["many"] = True
	# 		user = request.POST.get('user')
	# 		project = request.POST.get('project[1]')
	# 		task_data = TaskSerializer(data=request.data)
	# 		if not(task_data.is_valid()):
	# 			return Response(task_data.errors)
	# 		task_data.save()
	# 		return Response(task_data.data,status=status.HTTP_201_CREATED)
	# 	except Exception as err:
	# 		print(err)
			# return Response("Error")

	def get(self,request):
		
		task_data = Tasks.objects.all()
		return task_data
		
	def post(self,request):
		try:
			task_created = []
			for list_data in request.data:
				task_created.append(list_data)
			task_serializer = TaskSerializer(data=task_created, many=True)
			if not(task_serializer.is_valid()):
				return Response(task_serializer.errors)
			task_serializer.save()
			print(task_serializer.data[:])
			return Response(task_serializer.data[:],status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error")

## written by aarti
class UserTaskDatewise(APIView):
	def get(self,request,user_id=None):
		return render(request,'datewise_all_details.html')

	def post(self,request):
		usertasks = Tasks.objects.all()
		user_tasks = TaskSerializer(usertasks,many=True)
		return Response(user_tasks.data,status=status.HTTP_201_CREATED)
	
##Written By Ashwin
class CalculateHrs(APIView):
	def get(self,request,user_id):
		one_week_ago = datetime.today() - timedelta(days=7)
		get_week_tasks = Tasks.objects.filter(date__gte=one_week_ago,user_id=user_id)
		task_data = TaskSerializer(get_week_tasks,many=True)
		return Response(task_data.data,status=status.HTTP_201_CREATED)

	def post(self,request,user_id):
		one_month_ago = datetime.today() - timedelta(days=30)
		get_month_tasks = Tasks.objects.filter(date__gte=one_month_ago,user_id=user_id)
		month_data = TaskSerializer(get_month_tasks,many=True)
		return Response(month_data.data,status=status.HTTP_201_CREATED)

class GetTask(TemplateView):
	def get(self,request):
		return render(request,'get_task_list.html')

class GetUsersTasks(APIView):
	def get(self,request,task_id=None):
		print("ko")
		# get_user_tasks = Tasks.objects.get(user_id=task_id)
		# user_tasks = TaskSerializer(get_user_tasks,many=True)
		return Response(status=status.HTTP_201_CREATED)
