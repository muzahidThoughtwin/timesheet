# from django.contrib.auth import authenticate
# from rest_framework.decorators import authentication_classes, permission_classes
# from app.users.permissions import IsAuthenticatedOrCreate
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
from django.utils import timezone 

## written by aarti
class TaskView(APIView):

	def get(self,request,task_id=None):
		if request.GET.get('user') and request.GET.get('date'): 
			get_task = Tasks.objects.filter(user=request.GET.get('user'), date=request.GET.get('date'))
			task_data = TaskSerializer(get_task, many=True)
		elif task_id:
			get_task = Tasks.objects.filter(id=task_id)
			task_data = TaskSerializer(get_task, many=True)
		else:
			get_task = Tasks.objects.all()
			task_data = TaskSerializer(get_task, many=True)
		return Response(task_data.data,status=status.HTTP_201_CREATED)
		
	def post(self,request):
		try:
			task_data = TaskSerializer(data=request.data)
			if not(task_data.is_valid()):
				return Response(task_data.errors)
			task_data.save()
			return Response(task_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error")
		
	def put(self,request,task_id):
		try:
			get_data = Tasks.objects.get(pk=task_id)
			date_diff = (datetime.now().date() - get_data.date).days
			if (date_diff < 6):
				update_data = TaskSerializer(get_data, data=request.data)
				if update_data.is_valid():
					update_data.save()
					return Response("Task details updated Successfully")
				else:
					return Response(update_data.errors)			
			return Response("you are not able to update" ,status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			print(err)
			return Response("Error" ,status=status.HTTP_400_BAD_REQUEST)


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
