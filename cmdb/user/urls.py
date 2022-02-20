from django.urls import path
from .views import index, login, logout, del_user, edit_user, create

app_name = 'user'

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('del_user/', del_user, name='del_user'),
    path('edit_user/', edit_user, name='edit_user'),
    path('create/', create, name='create'),
]
