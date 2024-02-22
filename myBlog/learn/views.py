from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    # return HttpResponse('<h1>learn Home</h1>')

    features = Feature.objects.all()

    return render(request, 'learn/index.html', {'features': features})

def counter(request):
    features = Feature.objects.all()
    return render(request, 'learn/counter.html', {'features': features})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'learn/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'learn/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    f = Feature.objects.get(name=pk)
    return render(request, 'learn/post.html', {'pk': pk, 'f': f})