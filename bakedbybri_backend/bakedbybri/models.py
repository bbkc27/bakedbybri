from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Ingredients(models.Model):
  name = models.CharField(max_length=200, default='')

  def __str__(self):
    return self.name

class Post(models.Model):
  uuid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)
  author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=100, default='A Baked By Bri Recipe')
  ingredients = models.ManyToManyField(Ingredients, related_name='post_list', blank=True)
  duration = models.DurationField()
  category = models.CharField(max_length=100, default='')
  recipe = models.TextField(default='')

  def __str__(self):
    return self.title