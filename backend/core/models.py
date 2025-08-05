from django.db import models

# Create your models here.
class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    language = models.CharField(max_length=25, null=True, blank=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    video_link = models.URLField(help_text="Telegram Video Link")
    language = models.CharField(max_length=25)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"