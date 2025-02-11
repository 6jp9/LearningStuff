from django.shortcuts import render
from testapp.models import Students

def test(request):
    x = Students.objects.all()
    my_dict = {'my_dict': x}    
    return render(request, 'testapp/index.html', my_dict)
