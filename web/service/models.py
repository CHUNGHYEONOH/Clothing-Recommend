from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cloth(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    #def get_absolute_url(self):
    #    return reverse('photo:detail', args=[self.id])

