from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return render(request,'recipes/home.html',context={'nome': 'bruno santos'})

def contato(request):
   return HttpResponse('contato1')


def sobre(request):
   return HttpResponse('sobre2')