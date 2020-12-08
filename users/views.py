from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username %s password %s' %(username, password))
        
        user = User.objects.create(username=username, password=password)
        print(user)
        
        return HttpResponse('正在进行注册')