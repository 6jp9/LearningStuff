from django.shortcuts import render
# Create your views here.
from testapp.models import  Movies
from testapp.forms import MoviesForm
''

# Create your tests here.
def home(request):
    return render(request,'testapp/index.html')

def display_movies(request):
    movies = Movies.objects.all()
    return render(request,'testapp/list.html',{'movies':movies})

def movie_form(request):
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('success!!!')
    form = MoviesForm()
    return render(request,'testapp/add.html',{'form':form})




