from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from .models import Message
from django.db import models
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home', user_id=request.user.id)
    else:
        return render(request, 'index.html')

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
                messages.error(request,'Passwords did not match')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,phone_no=phone_no,password=password)
                user.save()

                login(user=user,request=request)

                return redirect('home',user_id=user.id)
        else:
            messages.error(request,'Passwords did not match')
            return redirect('signup')
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            return redirect('home',user_id=user.id)

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def home(request,user_id):
    all_users = get_user_model().objects.exclude(id=request.user.id).filter(is_superuser=False)

    messages = Message.objects.filter(
        models.Q(sender=request.user) | models.Q(receiver=request.user)
    ).order_by('timestamp')


    chat_users = []
    for message in messages:
        if message.sender != request.user:
            chat_users.append(message.sender)
        else:
            chat_users.append(message.receiver)

    unique_users = list(set(chat_users))

    return render(request, 'index.html', {
        'chat_users': unique_users,
        'all_users': all_users,
        'user_id':request.user.id
    })


@login_required
def chat_log(request, user_id):
    current_user = request.user
    chat_user = get_object_or_404(get_user_model(), id=user_id)

    messages = Message.objects.filter(
        models.Q(sender=current_user, receiver=chat_user) |
        models.Q(sender=chat_user, receiver=current_user)
    ).order_by('timestamp')
    print(f"Messages between {current_user} and {chat_user}: {messages}")
    messages_data = [
        {
            "sender": message.sender.username,
            "receiver": message.receiver.username,
            "content": message.message,
            "timestamp": message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for message in messages
    ]
    print(f"Messages Data: {messages_data}")

    return JsonResponse({'messages':messages_data})

def get_messages(request, user_id):
    messages = Message.objects.filter(id=user_id)
    data = {
        'messages': [{'sender': msg.sender.username, 'content': msg.content} for msg in messages]
    }
    return JsonResponse(data)
