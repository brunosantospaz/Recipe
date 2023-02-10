from django.contrib import admin
from .models import category

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    ...
    

admin.site.register(category, categoryAdmin)