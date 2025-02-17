from django.db import models

# Create your models here.
class StdDob(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=10)
    date_of_birth = models.DateField()
