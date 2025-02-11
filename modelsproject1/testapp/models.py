from django.db import models

# Create your models here.
class Test_table_IT(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    salary = models.IntegerField()
    eligibility = models.CharField(max_length=20)
    link = models.TextField()
class Test_table_Gov(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    eligibility = models.CharField(max_length=20)
    link = models.TextField()
