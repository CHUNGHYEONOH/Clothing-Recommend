from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    objects = models.Manager()
    image = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    price = models.FloatField()
    score = models.FloatField()