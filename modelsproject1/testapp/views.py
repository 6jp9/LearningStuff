from django.shortcuts import render
from testapp.models import Test_table_Gov,Test_table_IT

# Create your views here.
def index(request):
    return render(request, 'testapp/index.html')
def test_view_IT(request):
    x = Test_table_IT.objects.all()
    my_dir_IT = {'IT': x}
    return render(request, 'testapp/test_IT.html', my_dir_IT)
def test_view_Gov(request):
    x = Test_table_Gov.objects.all()
    my_dir_Gov = {'Gov': x}
    return render(request, 'testapp/test_Gov.html',my_dir_Gov)
