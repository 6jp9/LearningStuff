from django.http import HttpResponse
class ExecutionFlowMiddleware:
    def __init__(self,get_response):
        print('initilized')
        self.get_response = get_response
    def __call__(self,request):
        print('call executed')
        response = self.get_response(request)
        print('response raised')
        return response
    def process_exception(self,request,exception):
        return HttpResponse('<h1>Error detected</h1>')
