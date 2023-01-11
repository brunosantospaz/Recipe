from django.urls import path
from recipes.views import home,sobre




urlpatterns = [
    path('', home), #/home
    path('sobre/', sobre), #/sobre
   ]