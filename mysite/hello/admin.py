from django.contrib import admin
from .models import Movie,Task,Category,Actor
# Register your models here.
myModels = [Movie,Task,Category,Actor]
admin.site.register(myModels)
