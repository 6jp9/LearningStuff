from django.db import models

# Create your models here.
class Std(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.IntegerField()
