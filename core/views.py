from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def home_view(request):
  return HttpResponse("Заглушка: главная")

def catalog_view(request):
  return HttpResponse("Заглушка: каталог")

def movie_detail_view(request, pk):
  return HttpResponse(f"Заглушка: фильм {pk}")

def profile_view(request):
  return HttpResponse("Заглушка: профиль")

def register_view(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile')
  else:
    form = CustomUserCreationForm()
  return render(request, 'register.html', {'form': form})