from django.shortcuts import render
from testapp.forms import RegistrationForm

# Create your views here.
def registration_form(request):
    form = RegistrationForm()
    submit = False
    user = ''
    if request.method == "POST":
        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('success!!!')
            print('#'*30)
            print('Name:',form.cleaned_data['name'])
            print('email:',form.cleaned_data['email'])
            print('Contact:',form.cleaned_data['phone'])
            print('Password:',form.cleaned_data['password'])
            submit = True
            user=form.cleaned_data['name']
    
    

    return render(request,'testapp/index.html',{'form':form, 'submit': submit, 'name':user})