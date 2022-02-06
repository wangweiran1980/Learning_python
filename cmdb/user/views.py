from django.shortcuts import render
from .models import get_users

# Create your views here.


def index(request):
    users = get_users()
    if users[0]:
        return render(request, 'user/index.html', {'users': users[0].items()})
    return render(request, 'user/404.html', {'error': users[-1]})
