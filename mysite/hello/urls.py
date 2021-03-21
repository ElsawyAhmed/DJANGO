from django.urls import path, include
from rest_framework import routers
from . import views
from .apis.views import MovieAPI


router = routers.DefaultRouter()
router.register(r'movies', MovieAPI)


urlpatterns = [
    path('<str:name>' , views.helloIndex , name = 'helloIndex'),
    path('tasks/' , views.addTask , name = 'tasks'),
    path('' , views.empty , name = 'index'),
    path('remove/<str:Id>' , views.remove ,name = 'remove' ),
    path('towatch/' , views.to_watch , name = 'towatch'),
    path('removeMovie/<int:ID>', views.removeMovie , name='removeMovie' ),
    path('addMovie/' , views.addMovie, name='addMovie'),
    path('editMovie/<int:pk>' , views.editMovie, name='editMovie'),
    path('api/', include(router.urls)),
    path('apis/', include('hello.apis.urls'))
    # path('CRUDMovies/', include('rest_framework.urls', namespace='rest_framework'))
    
]



