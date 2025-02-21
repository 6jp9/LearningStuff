from django.shortcuts import render
from testapp.forms import TestForm
# Create your views here.
def display_form(request):
    
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            request.session[name] = quantity
            print('*'*60)
            request.session.set_expiry(20)
            print(request.session.get_expiry_date())
    form = TestForm()
    return render(request,'testapp/index.html',{'form':form})

def data(request):
    return render(request,'testapp/table.html')

