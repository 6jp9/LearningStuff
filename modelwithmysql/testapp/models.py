from django.db import models

# Create your models here.
class emp(models.Model):
    empName = models.CharField(max_length=30)
    empID = models.IntegerField()
    empAddress = models.TextField()
    empContact = models.BigIntegerField()