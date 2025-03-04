from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Movies
from django.urls import reverse_lazy

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

class MoviesUpdateView(UpdateView):
    model = Movies
    fields = '__all__'
    template_name = 'testapp/create.html'

class MoviesDeleteView(DeleteView):
    model = Movies
    context_object_name = 'movies'
    success_url = reverse_lazy('home')
