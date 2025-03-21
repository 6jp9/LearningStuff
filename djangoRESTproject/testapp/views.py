from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from testapp.models import Movies
from testapp.serilizer import MoviesSerializer
import io
from django.http import HttpResponse


#to create a record in database from json(third-party or external source) we need to disable csrf token.
#we can disable it from settings by commenting it. but it will be disable for entire project apps. which might be a problems in future.
#by using the below decorator we can disable it for the following class. 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
#in name='dispatch' means it is disabled for the entire class. you can also mention function name to disable it for a certain view
#ex: name='post'


# Create your views here.



class MoviesCURDcbv(View):
#to update the existing data using put()
    def put(self,request,*args,**kwargs):
        tjd = request.body
        stream = io.BytesIO(tjd)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        movie = Movies.objects.get(id=id)
        mser = MoviesSerializer(movie,data = pdata, partial=True) #patrial=True to update only certain field,
                                        #movie carries the record and data=pdata will give what data to update in the record
        if mser.is_valid():
            mser.save()
            msg = {'msg':'success!!!'}
            jd = JSONRenderer().render(msg)
            return HttpResponse(jd, content_type='application/json')
        jd = JSONRenderer().render(mser.errors)
        return HttpResponse(jd, content_type='application/json',status=400)
        


#to delete a record from database by passing id from json
    def delete(self,request,*args,**kwargs):
        js = request.body
        stream = io.BytesIO(js)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        rec = Movies.objects.get(id=id)
        rec.delete()
        msg = {'msg':'success!!!!'}
        jd = JSONRenderer().render(msg)
        return HttpResponse(jd,content_type = 'application/json')



#to create new record into database from json
    def post(self,request,*args,**kwargs):
        js = request.body
        stream = io.BytesIO(js)
        pdata = JSONParser().parse(stream)
        mser = MoviesSerializer(data = pdata)
        if mser.is_valid():
            mser.save()
            msg = {'msg':'success!!!!'}
            jd = JSONRenderer().render(msg)
            return HttpResponse(jd,content_type = 'application/json')
        jd = JSONRenderer().render(mser.errors)
        return HttpResponse(jd,content_type = 'application/json',status=400)




#to display the data form data base in json formate
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            movie = Movies.objects.get(id=id)
            ser = MoviesSerializer(movie)
            jd = JSONRenderer().render(ser.data)
            return HttpResponse(jd, content_type = 'application/json',status=200)
        qs = Movies.objects.all()
        eser = MoviesSerializer(qs,many=True)
        jd = JSONRenderer().render(eser.data)
        return HttpResponse(jd, content_type='application/json',status=200)
    
    