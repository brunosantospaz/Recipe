from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=65)



class recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving_unit = models.IntegerField(max_length=65)
    serving = models.IntegerField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d')
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

#EDITED
#title desciption slug
#preparation_time preparation_time_unit
#serving serving_unit
#preparation_step
#preparation_step_is_html
#created_at update_at
#is_published
#cover
#category (relaçao)
# author (relaçao)