from django.contrib import admin
from django.urls import path , include

from first_app.views import home,singup,user_login,user_logout,profile,pass_change,pass_change2

urlpatterns = [
    path('', home,name='home'),
    path('singup/', singup ,name='singup'),
    path('login/', user_login ,name='login'),
    path('logout/', user_logout,name='logout' ),
    path('profile/', profile,name='profile'),
    path('password_change/', pass_change,name='pass_change'),
    path('password_change2/', pass_change2,name='pass_change2'),
]
