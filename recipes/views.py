from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import recipe

def home(request):
     recipes = recipe.objects.all().order_by('-id')
     return render(request, 'recipes/pages/home.html', context={
         'recipes': recipes,
     })

def category(request, category_id):
     recipes = recipe.objects.filter(
         category__id=category_id
     ).order_by('-id')
     return render(request, 'recipes/pages/home.html', context={
         'recipes': recipes,
     })



