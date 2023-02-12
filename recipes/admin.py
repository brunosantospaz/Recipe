from django.contrib import admin
from .models import category, recipe

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    ...
    
@admin.register(recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(category, categoryAdmin)