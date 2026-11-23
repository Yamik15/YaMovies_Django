from django.db import models
from django.contrib.auth.models import AbstractUser # в нем уже присутствуют email & password

class User(AbstractUser):
  full_name = models.CharField(max_length=255, blank=True, verbose_name="ФИО")
  birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
  gender = models.CharField(max_length=10, choices=[("M", "Мужской"), ("F", "Женский")], blank=True, verbose_name="Пол")
  
  def __str__(self):
    return self.username
  
class Genre(models.Model):
  title = models.CharField(max_length=100, verbose_name="Название жанра")
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
			return self.title
	
class Movie(models.Model):
  title = models.CharField(max_length=255, verbose_name="Название")
  original_title = models.CharField(max_length=255, blank=True, verbose_name="Оригинальное название")
  year = models.IntegerField(verbose_name="Год выпуска")
  description = models.TextField(verbose_name="Описание")
  rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies", verbose_name="Жанр")
  poster_name = models.CharField(max_length=100, help_text="Имя файла в static/images/posters/", verbose_name="Постер")
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
			return self.title
	
class Review(models.Model):
  description = models.TextField(verbose_name="Текст отзыва")
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="revies", verbose_name="Фильм")
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="revies", verbose_name="Пользователь")
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
			return f"Отзыв от {self.user.username} на {self.movie.title}"