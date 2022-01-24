from django.shortcuts import render
import time
# from django.http import HttpResponse

# Create your views here.

users = {
    '1': {
        'name': 'Jack',
        'gender': 1,
        'age': 20,
        'tel': '987'
    },
    '2': {
        'name': 'Rose',
        'gender': 0,
        'age': 16,
        'tel': '765'
    },
}


def index(request):
    # return HttpResponse('我的第一个网页')
    # return render(request, 'user/index.html')
    return render(request, 'user/index.html', {
        'current_time': time.time(),
        'users': users.items()
    })
