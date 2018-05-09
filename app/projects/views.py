from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
# from app.users.permissions import IsAuthenticatedOrCreate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.projects.serializers import ProjectSerializer
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.projects.models import Projects
from django.contrib.auth.models import User

## written by aarti
class ProjectView(APIView):
	
	def post(self,request):
		try:
			project_data = ProjectSerializer(data=request.data)
			if not(project_data.is_valid()):
				return Response(project_data.errors)
			project_data.save()
			return Response("Project created successfully",status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating project")

	def get(self,request,project_id=None):
		try:
			if(project_id):
				project_data = Projects.objects.get(pk=project_id)
				get_data = ProjectSerializer(project_data)
			else:
				project_data = Projects.objects.all()
				get_data = ProjectSerializer(project_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")

	def put(self,request,project_id):
		try:
			get_data = Projects.objects.get(pk=project_id)
			update_data = ProjectSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("Project details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

