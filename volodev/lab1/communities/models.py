from django.db import models
from django.contrib.auth.models import User

class Communitie(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150, default='no discription')
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
