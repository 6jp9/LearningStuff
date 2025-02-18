from django.shortcuts import render

# Create your views here.
def test(request):
    count = int(request.COOKIES.get('count',0))
    count += 1
    response = render(request,'testapp/index.html',{'count' : count})
    response.set_cookie('count',count)
    return response
