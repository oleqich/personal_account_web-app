from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    bio = models.TextField("bio", max_length = 300, blank=True)
    