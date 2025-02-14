from django import forms
from testapp.models import Movies

class MoviesForm(forms.ModelForm):
    name = forms.CharField()
    hero = forms.CharField()
    heroine = forms.CharField()
    rating = forms.IntegerField()
    class Meta:
        model = Movies
        fields = '__all__'
