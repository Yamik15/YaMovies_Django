from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Genre, Movie, Review

class CustomUserAdmin(UserAdmin):
  fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('full_name', 'birth_date', 'gender')}),
	)
  
admin.site.register(User, CustomUserAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)