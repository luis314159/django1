from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username ='no user name'):
 
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return HttpResponse("<h1>About</h1>")

def projects(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe = False)

def tasks(request,title):
    #task = Task.objects.get(id=id) 
    task = get_object_or_404(Task, title=title)
    #task = Task.objects.get(title=title) 
    return HttpResponse('task: %s '% task.title)