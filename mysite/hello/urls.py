from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>' , views.helloIndex , name = 'helloIndex'),
    path('tasks/' , views.addTask , name = 'tasks'),
    path('' , views.empty , name = 'index'),
    path('remove/<str:Id>' , views.remove ,name = 'remove' ),
    path('towatch/' , views.to_watch , name = 'towatch'),
    path('removeMovie/<int:ID>', views.removeMovie , name='removeMovie' ),
    path('addMovie/' , views.addMovie, name='addMovie'),
    path('editMovie/<int:movId>' , views.editMovie, name='editMovie'),
    
]