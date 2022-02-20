from django.shortcuts import render, redirect
from .models import User
from datetime import datetime

# Create your views here.


def index(request):
    if not request.session.get('username'):
        return redirect('user:login')
    users = User.objects.all()
    if users:
        return render(request, 'user/index.html', {'users': users})
    return render(request, 'user/404.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        if User.verify_login(username, password):
            request.session['username'] = username
            return redirect('user:index')
        return render(request, 'user/login.html', {'error': '账户或密码错误!'})


def logout(request):
    if not request.session.get('username'):
        return redirect('user:login')
    request.session.flush()
    return redirect('user:login')


def del_user(request):
    if not request.session.get('username'):
        return redirect('user:login')
    uid = request.GET.get('uid')
    try:
        User.objects.get(pk=uid).delete()
    except BaseException:
        return redirect('user:index')
    return redirect('user:index')


def edit_user(request):
    if not request.session.get('username'):
        return redirect('user:login')
    if request.method == 'GET':
        uid = request.GET.get('uid')
        user = User.objects.get(pk=uid)
        if user:
            return render(request, 'user/edit.html', {'user': user})
    elif request.method == 'POST':
        uid = request.POST.get('uid')
        try:
            user = User.objects.get(pk=uid)
            if user:
                user.username = request.POST.get('username').strip()
                user.gender = int(request.POST.get('gender').strip())
                user.age = request.POST.get('age').strip()
                user.tel = request.POST.get('tel').strip()
                user.pwd = request.POST.get('password')
                user.save()
        except BaseException as err:
            print(err)
            return redirect('user:index')
        return redirect('user:index')


def create(request):
    if not request.session.get('username'):
        return redirect('user:login')

    if request.method == 'GET':
        return render(request, 'user/user.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username').strip()
        user.gender = int(request.POST.get('gender').strip())
        user.age = request.POST.get('age')
        user.tel = request.POST.get('tel').strip()
        user.pwd = request.POST.get('password')
        user.create_time = datetime.now()
        try:
            user.save()
        except BaseException:
            return redirect('user:index')
    return redirect('user:index')
