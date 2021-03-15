from django.db import models

# Create your models here.
class Shehata(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_priority = models.IntegerField()
