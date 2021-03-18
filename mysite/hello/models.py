from django.db import models

# Create your models here.
class Rate(models.Model):#=======================
    rate_value = models.IntegerField(range(0,5) , blank = True , null = True )
    def __str__(self):
        return (f' {self.rate_value} ')

class Actor(models.Model):
    actor_name = models.CharField(max_length = 50)
    actor_nationality = models.CharField(max_length = 20)
    actor_personal_image = models.ImageField(upload_to = 'actors/pictures')
    birth_date = models.DateField()

    def __str__(self):
        return (f'{self.actor_name}')



class  Category(models.Model):
    category_name = models.CharField(max_length = 100)
    category_description = models.CharField(max_length = 150)

    def __str__(self):
        return (f' {self.category_name}  ')


class Movie(models.Model):
    Id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    img = models.TextField()
    movie_file = models.FileField(upload_to = 'movies/') #--> done
    movie_category = models.ManyToManyField(Category)   #new ---> done
    movie_rate = models.OneToOneField(Rate , null = True , on_delete = models.SET_NULL)
    movie_actors = models.ForeignKey(Actor, null = True , on_delete = models.SET_NULL)

    def __str__(self):
        return (f' Movie {self.title}|{self.movie_category}')

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_priority = models.IntegerField() #take care  -->

    def __str__(self):
        return (f'{self.task_name}')


#new 


# class Customer(models.Model):
#     customer_name = models.CharField(max_length = 50)
#     customer_age = models.IntegerField