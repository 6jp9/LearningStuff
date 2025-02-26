from django import forms
from testapp.models import Std

class InsertForm(forms.ModelForm):
    class Meta:
        model = Std
        fields = '__all__'
