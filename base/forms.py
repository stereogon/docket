from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Task

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'description']
