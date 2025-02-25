from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import Sign_up
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def pytest_view(request):
    return render(request,'testapp/pytest.html')

@login_required
def sqltest_view(request):
    return render(request,'testapp/sqltest.html')

def logout_view(request):
    return render(request,'registration/logout.html')

def signup_view(request):
    form = Sign_up()
    if request.method == 'POST':
        form = Sign_up(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'registration/signup.html',{'form':form})