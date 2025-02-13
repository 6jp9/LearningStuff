from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    bot_validation = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean(self):
        validation = super().clean()
        val_name = validation['name']
        if len(val_name) < 4:
            raise forms.ValidationError('name characters should be > 4')
        val_pass = validation['password']
        val_rpas = validation['rpassword']
        if val_pass != val_rpas:
            raise forms.ValidationError('password did not match!!!!')
        


