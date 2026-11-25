from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ReviewForm
from .models import Movie, Genre, Review

def home_view(request):
  return render(request, 'home.html')

def catalog_view(request):
  movies = Movie.objects.all()
  genres = Genre.objects.all()
  genre_id = request.GET.get('genre')
  if genre_id:
    movies = movies.filter(genre_id=genre_id)
  return render(request, 'catalog.html', {'movies': movies, 'genres': genres})

def movie_detail_view(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  return render(request, 'movie_detail.html', {'movie': movie})

@login_required
def profile_view(request):
  reviews = request.user.reviews.all().order_by('-created_at')
  
  if request.method == 'POST':
    action = request.POST.get('action')
    
    if action == 'add':
      form = ReviewForm(request.POST)
      if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('profile')
      
    elif action == 'delete':
      review_id = request.POST.get('review_id')
      Review.objects.filter(id=review_id, user=request.user).delete()
      return redirect('profile')
    
  else:
    initial = {}
    movie_id = request.GET.get('movie')
    if movie_id:
      initial['movie'] = movie_id
    form = ReviewForm(initial=initial)
    
  return render(request, 'profile.html', {'reviews': reviews, 'form': form})

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