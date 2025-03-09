from django.db import models

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=30)
    ph_no = models.CharField(max_length=30)
    address = models.TextField()
    class Meta():
        abstract = True

class Student(Base):
    marks = models.FloatField()

class Teacher(Base):
    subject = models.CharField(max_length=20)
