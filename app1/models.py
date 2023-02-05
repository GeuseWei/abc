from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=16, default="")
    email = models.EmailField(default="")
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=16, default="")
    major = models.CharField(max_length=16, default="")
    occupation = models.CharField(max_length=16, default="")
    phone = models.IntegerField(default="")


class Passwords(models.Model):
    password = models.CharField(max_length=16, default="")
