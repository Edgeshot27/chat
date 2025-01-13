from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('chat/<int:user_id>/',views.chat_log,name='chat_log')
]