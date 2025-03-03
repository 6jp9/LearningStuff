from django.db import models
from django.urls import reverse

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    rating = models.IntegerField()
    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})