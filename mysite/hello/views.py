from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect

# Create your views here.

tasks = {'1':'Go To Finalize your exam', '2':'finish this lab'}
author = 'Elsawy'

def helloIndex(request , name):
    return HttpResponse(f'<h1>Welcome {name}</h1>')

def addnew(request ):
    if request.POST:
        print(request)
        if request.POST.get('new') != '':
            tasks[f'{len(tasks)+1}'] = request.POST.get('new')
            return HttpResponseRedirect('')
    
    return render(request ,'hello/tasks.html', {'tasks': tasks,'name':author})

def empty(request):
    return render(request , "hello/layout.html" , {'name' : author})

def remove(request,Id):
    tasks.pop(f'{Id}')
    return redirect('tasks')