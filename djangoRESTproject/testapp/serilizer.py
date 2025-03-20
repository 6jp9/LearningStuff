from rest_framework import serializers
from testapp.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    model = Movies
    fields = '__all__'
