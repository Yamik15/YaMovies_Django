from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
  return HttpResponse("Заглушка: главная")

def catalog_view(request):
  return HttpResponse("Заглушка: каталог")

def movie_detail_view(request, pk):
  return HttpResponse(f"Заглушка: фильм {pk}")

def profile_view(request):
  return HttpResponse("Заглушка: профиль")

def register_view(request):
  return HttpResponse("Заглушка: регистрация")