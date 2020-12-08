from django.http import HttpResponse
# Create your views here.


def first_view_func(request):
    return HttpResponse('<h1>helloworld</h1>')
