from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredients(models.Model):
  name = models.CharField(max_length=200, default='')

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey(User, related_name='Author', on_delete=models.CASCADE, default='Bri')
  title = models.CharField(max_length=100, default='A Baked By Bri Recipe')
  ingredients = models.ManyToManyField(Ingredients, related_name='ingredients', blank=True)
  duration = models.DurationField()
  category = models.CharField(max_length=100, default='')
  recipe = models.TextField(default='')

  def __str__(self):
    return self.title