from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Androidapp(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
class AppDownload(models.Model):
    app = models.ForeignKey(Androidapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
class User(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    points_earned = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)
class Profile(models.Model):
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
