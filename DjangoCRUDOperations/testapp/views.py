from django.shortcuts import render,redirect
from testapp.models import Std
from testapp.forms import InsertForm
# Create your views here.
def home_view(request):
    std_data = Std.objects.all()
    return render(request,'testapp/index.html',{'students':std_data})
def insert_view(request):
    form = InsertForm()
    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})

def del_data(request,roll):
    temp = Std.objects.get(roll=roll)
    temp.delete()
    return redirect('/')

