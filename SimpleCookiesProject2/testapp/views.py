from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')


def gender(request):
    user = request.GET['name']
    r = render(request,'testapp/gender.html',{'name':user})
    r.set_cookie('name',user)
    return r


def dob(request):
    user = request.COOKIES['name']
    gender = request.GET['gender']
    r = render(request,'testapp/dob.html',{'name':user})
    r.set_cookie('gender',gender)
    return r

def result(request):
    user = request.COOKIES['name']
    gender = request.COOKIES['gender']
    dob = request.GET['dob']
    return render(request,'testapp/result.html',{'name':user,'gender':gender,'dob':dob})
