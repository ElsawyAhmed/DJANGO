from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>' , views.helloIndex , name = 'helloIndex'),
    path('tasks/' , views.addnew , name = 'tasks'),
    path('' , views.empty , name = 'index'),
    path('remove/<str:Id>' , views.remove ,name = 'remove' )
]