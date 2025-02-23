from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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