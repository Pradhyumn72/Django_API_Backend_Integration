from django.db import models

# Create your models here.
class Studentt(models.Model):
    name=models.CharField(max_length=16)
    email=models.EmailField(unique=True)
    contact=models.CharField(unique=True,max_length=10)