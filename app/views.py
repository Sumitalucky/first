from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def susmita(request):
              return HttpResponse('<h1>Hello</h1>')
def sample(request):
              return HttpResponse('<marquee><h1>Good Evening</h1></marquee>')
def student(request):
              return HttpResponse('<marquee><h1>we are groot</h1></marquee>')