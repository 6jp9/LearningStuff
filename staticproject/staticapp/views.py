from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'staticapp/index.html')

def test1(request):
    return render(request,'staticapp/1.html')
def test2(request):
    return render(request,'staticapp/2.html')
