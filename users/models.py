from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # Creates image for all users on their profile page
    avatar = models.ImageField(blank=True, null=True, default='avatars/default.png')
