from django.db import models

# Create your models here.
class CustomEno(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('emp_name')
    def orderWith(self,record):
        return super().get_queryset().order_by(record)
    def Id_range(self,minval,maxsal):
        return super().get_queryset().filter(emp_id__range=(minval,maxsal))




class Employees(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    emp_addr = models.TextField()
    objects = CustomEno()


