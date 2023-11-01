from django.shortcuts import render
from .models import Project

def home(request):
        return render(request, 'alphonce/home.html')

def index(request):
        projects = Project.objects.all()
        context = {
                "projects": projects
        }
        return render(request, 'alphonce/index.html')