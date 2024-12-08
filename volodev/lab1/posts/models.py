from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150, default='Нет описания')
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.name



