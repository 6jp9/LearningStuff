from django.shortcuts import render

# Create your views here.
from testapp.models import Employees
def test_view(request):
    # data = Employees.objects.all()
    # data = Employees.objects.Id_range(1000,3000)
    data = Employees.objects.orderWith('emp_name')# '-emp_name' for descending order

    return render(request,'testapp/index.html',{'emp':data})
