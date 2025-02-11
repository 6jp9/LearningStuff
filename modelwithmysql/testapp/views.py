from django.shortcuts import render
from testapp.models import emp

# Create your views here.
def test_display(request):
    x = emp.objects.all()
    my_dict={'my_dict':x}
    return render(request, 'testapp/index.html',my_dict)



