from django.shortcuts import render
from .models import Project

def home(request):
        return render(request, 'alphonce/home.html')

def index(request):
        projects = Project.objects.all()
        context = {
                "projects": projects
        }
        return render(request, 'alphonce/index.html', context)

def detail(request, pk):
        project = Project.objects.get(pk=pk)
        context = {
        "project": project
       }
        return render(request, 'alphonce/detail.html', context)


def about(request):
        