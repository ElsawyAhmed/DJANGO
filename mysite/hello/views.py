from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from hello.models import Task, Movie, Category, Actor
from .forms import editMovieForm
from  django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

tasks = {'1':'Go To Finalize your exam', '2':'finish this lab'}
author = 'Elsawy'



def helloIndex(request , name):
    return HttpResponse(f'<h1>Welcome {name}</h1>')

def addTask(request ):
    if request.POST:
        print(request)
        if request.POST.get('new') != '':
            tasks[f'{len(tasks)+2}'] = request.POST.get('new')
            return HttpResponseRedirect('')
    
    return render(request ,'hello/tasks.html', {'tasks': tasks,'name':author})

def empty(request):
    return render(request , "hello/layout.html" , {'name' : author})

def remove(request,Id):
    tasks.pop(f'{Id}')
    return redirect('tasks')

@login_required
def to_watch(request):
    return render(request , 'hello/toWatch.html',{'movies':Movie.objects.all()})

@login_required
@permission_required
def removeMovie(request , ID):
    mov = Movie.objects.get(Id=ID)
    mov.delete()
    return redirect('towatch')

@login_required
@permission_required('hello.add_movie')
def addMovie(request):
    if request.POST:
            movie = Movie(request.POST.get('movId'),request.POST.get('movTitle')
                        ,request.POST.get('movUrl') , request.POST.get('movfile')) 
            
            movie.save()
    return render(request,'hello/addMovie.html',{'categories': Category.objects.all()})

@login_required
@permission_required
def editMovie(request,movId):
    movie = Movie.objects.get(Id=movId)
    return render(request,'hello/editMovie.html',{'movie':movie})

