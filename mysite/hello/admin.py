from django.contrib import admin
from .models import Movie,Task,Category,Actor,Rate
# Register your models here.
myModels = [Task,Actor,Rate]


class MovieAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-Value'
    list_display = ('title', 'movie_rate')
    
@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'Not Assigned Yet'
    list_display = ('category_name','category_description')

    # list_filter = ('category_name') #-->Not Valid filter by list or tuple

# class MovieInline(TabularInline):
#     model = Movie
#     extra  = 2
#     max_num = 5
admin.site.register(Movie,MovieAdmin)

admin.site.register(myModels)