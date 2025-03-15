from rest_framework import serializers
class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    hero = serializers.CharField(max_length=30)
    rating = serializers.IntegerField()

