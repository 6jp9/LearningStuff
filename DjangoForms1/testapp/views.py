from django.shortcuts import render

# Create your views here.
from testapp.forms import Feedback_form

def test_view(request):
    submitted = False
    name = ''
    if request.method == 'POST':
        form = Feedback_form(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*'*55)
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
    form = Feedback_form()
    return render(request,'testapp/index.html',
    {'form':form,'submitted':submitted,'name':name})



