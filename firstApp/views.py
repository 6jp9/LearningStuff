from django.shortcuts import render

# Create your views here.

def wish(Request):
    return render(Request, 'firstApp/index.html')
