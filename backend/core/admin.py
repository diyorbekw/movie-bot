from django.contrib import admin
from .models import Movie, User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'telegram_id', 'phone_number', 'language']
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'language']