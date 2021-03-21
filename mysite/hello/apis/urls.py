from django.urls import path
from . import views
from rest_framework import routers
from . import views

urlpatterns =[
    path('listmovies', views.listAll),
    path('addmovie', views.add_movie),
    path('deletemovie/<int:Id>', views.delete_movie),
    # path('updatemovie/<int:Id>', views.update_movie)
]