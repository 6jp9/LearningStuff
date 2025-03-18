from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from testapp.models import Movies
from testapp.serilizer import MoviesSerializer
import io
from django.http import HttpResponse

# Create your views here.
class MoviesCURDcbv(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        print('hello')
        if id is not None:
            movie = Movies.objects.get(id=id)
            ser = MoviesSerializer(movie)
            jd = JSONRenderer().render(ser.data)
            return HttpResponse(jd, content_type = 'application/json')
        