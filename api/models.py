from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class CSVData(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)