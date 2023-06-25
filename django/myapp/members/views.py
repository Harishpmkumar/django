from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import User
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User(name=name, email=email, phone=phone, password=password)
            user.save()
            return redirect('signin')
        else:
            error = 'Passwords do not match.'
            return render(request, 'register.html', {'error': error})
    else:
        return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)
            return redirect('index', user_id=user.id)
        except User.DoesNotExist:
            error = 'Invalid email or password.'
            return render(request, 'signin.html', {'error': error})
    else:
        return render(request, 'signin.html')

@login_required
def index(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'index.html', {'user': user})


def user_logout(request):
    logout(request)
    return redirect('signin')
