from django.http import HttpResponse

class Errormessagemiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("pre procesing request ")
        response = self.get_response(request)
        print("post procesing request ")
        return response
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Some thing went wrong {exception.__class__.__name__}</h1><br>'
                            f'<h1>exeption massage : {exception}</h1>')