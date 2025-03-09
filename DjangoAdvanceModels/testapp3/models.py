from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField()
class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()

class A(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        abstract = True
class B(models.Model):
    job = models.CharField(max_length=30)
    class Meta:
        abstract = True

class C(A,B):
    salary = models.FloatField()
