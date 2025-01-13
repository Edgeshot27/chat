from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from .models import Message
from django.db import models
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        User=get_user_model()
        username=request.POST['username']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        password=request.POST['password']
        re_password=request.POST['re_password']
        if password==re_password:
            if User.objects.filter(username=username).exists():
                messages.error('Passwords did not match')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,phone_no=phone_no,password=password)
                user.save()

                login(user=user,request=request)
                return redirect('chat_log',user_id=user.id)
        else:
            messages.error('Passwords did not match')
            return redirect('signup')
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('chat_log',user_id=user.id)
        else:
            messages.error('Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html')

@login_required
def home(request,user_id):
    user=get_object_or_404(get_user_model(),id=user_id)
    return render(request,'index.html',{'user':user})

@login_required
def chat_log(request,user_id):
    other_user=get_object_or_404(get_user_model(),id=user_id)
    message=Message.objects.filter((models.Q(sender=request.user)) & (models.Q(receiver=other_user)) | (models.Q(sender=other_user)) & (models.Q(receiver=request.user)))

    if request.method=='POST':
        content=request.POST['content']
        if content.strip():
            Message.objects.create(sender=request.user,receiver=other_user,content=content)
            return redirect('chat_log',user_id=user_id)
    return render(request,'chat_log.html',{'messages':message,'other_user':other_user})