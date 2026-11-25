from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Review

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  full_name = forms.CharField(required=True)
  birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  
  class Meta(UserCreationForm.Meta):
    model = User
    fields = ("username", "email", "full_name", "birth_date", "gender")
    
class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['movie', 'description']
    widgets = {
      'description': forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Напишите ваш отзыв...',
      }),
    }