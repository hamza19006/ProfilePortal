# profiles/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='defoult' , upload_to='profile_images')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
