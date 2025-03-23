from rest_framework import serializers
from testapp.models import Movies




class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


    def validate_rating(self,value):
        if value<8:
            raise serializers.ValidationError('rating must be greater than 8')
        return value
    

    def validate(self,data):
        mname = data.get('name')
        mrate = data.get('rating')
        print(mname)
        if mname.lower() == 'og':
            if mrate<9:
                raise serializers.ValidationError('for OG rating must be 10......')
        return data


