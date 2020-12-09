from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from users.models import User
import hashlib

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_word = hashlib.new('md5', (password+'123').encode('UTF-8')).hexdigest()
        print('username:%s password:%s' % (username, new_word))
        
        user = User.objects.create(username=username, password=new_word)
        print(user)
        
        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html', context={'username': username})
    
    else:
        #获取表单提交的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            # 与数据库进行对比
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            #如果注册账户里没有该用户
            return JsonResponse({'message': 'login failed!'})
        
        else:
            response = JsonResponse({'message': 'login succeed'})
        
            if remember == True:
                response.set_cookie('username', username, max_age=14 * 14 * 3600)
                
            return response
    
    