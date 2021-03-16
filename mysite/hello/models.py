from django.db import models

# Create your models here.
class Movie(models.Model):
    Id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    img = models.TextField()

    def __str__(self):
        return (f' {self.Id} ---> {self.title} ----> {self.img} ')

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_priority = models.IntegerField()
