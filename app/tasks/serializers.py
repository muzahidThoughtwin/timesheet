from rest_framework import serializers
from app.tasks.models import Tasks  
from app.projects.models import Projects
from app.projects.serializers import ProjectSerializer
from django.contrib.auth.models import User
from app.users.models import UserProfile,UserProjects
from app.users.serializers import UserSerializer

## written by aarti
class TaskSerializer(serializers.ModelSerializer):
	project_name = serializers.SerializerMethodField("getProjectDetail")
	def getProjectDetail(self,obj):
		try:
			return Projects.objects.get(id=obj.project.id).name
		except Exception as e:
			print(e)

	
	##Written By Ashwin
	user_name = serializers.SerializerMethodField("getUserName")
	def getUserName(self,obj):
		try:
			return UserProjects.objects.get(id=obj.project.id).id
			# return UserProfile.objects.get(first_name=obj.first_name)
			# return UserSerializer(UserProfile.objects.get(id=obj.project.id)).data
		except Exception as e:
			print(e)
		 
	class Meta:
		model =  Tasks
		fields = ('id','user','project_name','user_name','date','project','hours','description','is_billing','is_deleted','created_at','updated_at')
		extra_kwargs = {
				'hour': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			},
				'date': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}