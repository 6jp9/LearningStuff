from django.shortcuts import render
from testapp.forms import TestForm
# Create your views here.
def display_form(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['quantity'] = form.cleaned_data['quantity']
            print(request.COOKIES)
            print(request.session.get_expiry_age())
    return render(request,'testapp/index.html',{'form':form})

def data(request):
    name = request.session['name']
    quantity = request.session['quantity']
    return render(request,'testapp/table.html',{'name':name,'quantity':quantity})

