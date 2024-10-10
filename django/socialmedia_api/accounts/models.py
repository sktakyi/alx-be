from django.db import models
from django.contrib.auth.models import AbstractUser 

# Custom User Model utilizing Django’s built-in AbstractUser
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    
    def __str__(self):
        return self.username
