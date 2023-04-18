from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


def user_create(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    elif request.method == 'POST':
        first_name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_conf = request.POST.get('password-conf')

        message = {}
        if  len(first_name.strip()) == 0 or len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(password_conf.strip()) == 0:
            message['msg'] = 'Todos os campos são obrigatórios!'
            message['class'] = 'alert-danger'
            return render(request, 'registro.html', message)
        
        message = {}
        if password != password_conf:
            message['msg'] = 'Senhas e confirmação de senha diferentes!'
            message['class'] = 'alert-danger'
            return render(request, 'registro.html', message)
        
        try:
            user = User.objects.create_user(
                first_name = first_name,
                username=username,
                email=email,
                password=password
            )
            return redirect('login')
        except:
            return render(request, 'home.html')

    return render(request, 'home.html')


def user_login(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    message = {}
                    message['msg'] = 'Conta desativada!'
                    message['class'] = 'alert-danger'
                    return render(request, 'login.html', message)
            else:
                message = {}
                message['msg'] = 'Login e senha incorretos!'
                message['class'] = 'alert-danger'
                return render(request, 'login.html', message)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_profile(request):
    
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return render(request, 'home.html')
