from django.shortcuts import render
from testapp.models import Employees
from django.db.models import Q
# Create your views here.
def model_view(request):
    # table = Employees.objects.all()
    # table = Employees.objects.filter(esal__lt=30000)
    # table = Employees.objects.filter(esal__gte=30000)
    # table = Employees.objects.filter(id__in=[1,23,45])
    # table = Employees.objects.filter(id__in=(1,23,25))
    # table = Employees.objects.filter(ename__contains='Cod')
    # table = Employees.objects.filter(ename__startswith='A')
    # table = Employees.objects.filter(ename__endswith='e')
    # table = Employees.objects.filter(esal__range= [40000,60000])
    # table = Employees.objects.filter(Q(ename__contains='A') | Q(esal__range= [40000,60000]))
    # table = Employees.objects.filter(Q(ename__contains='A') & Q(esal__range= [40000,60000]))
    table = Employees.objects.filter(~Q(esal__range= [40000,60000])) # or exclude(esal__range=[40000,60000])
    return render(request,'testapp/index.html',{'model': table})
