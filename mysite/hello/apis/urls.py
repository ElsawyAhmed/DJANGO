from django.urls import path
from . import views
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'movies', views.MovieAPI)

urlpatterns =[

]