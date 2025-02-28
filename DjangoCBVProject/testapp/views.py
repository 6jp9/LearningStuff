from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Test(TemplateView):
    template_name = 'testapp/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Danny'
        context['roll'] = 69
        context['marks'] = 69
        return context
