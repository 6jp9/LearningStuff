from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from testapp.models import Movies

# Create your views here.
class MoviesListView(ListView):
    model = Movies

class MoviesDetailView(DetailView):
    model =Movies
    template_name = 'testapp/details.html'
    context_object_name = 'movie'

class MoviesCreateView(CreateView):
    model = Movies
    fields = '__all__'
    template_name = 'testapp/create.html'
