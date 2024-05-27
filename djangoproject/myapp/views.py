from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Welcome to Djanco course"
    return render(request, 'index.html', {
        'title': title
    })


def hello(request, username='no user name'):

    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    username = "M.I Luis Ángel Almazán López"
    # return HttpResponse("<h1>About</h1>")
    return render(request, 'about.html',
                  {"username": username}
                  )


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        # Save in DB
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        # Save in DB
        Project.objects.create(name=request.POST['name'])
        return redirect('prjects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    #project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=project.id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })