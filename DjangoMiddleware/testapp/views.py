from django.shortcuts import render

# Create your views here.
def index_view(request):
    #print(10/0)
    return render(request,'testapp/index.html')
