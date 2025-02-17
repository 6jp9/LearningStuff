from django import forms
from testapp.models import StdDob

class StdDobForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = StdDob
        fields = '__all__'