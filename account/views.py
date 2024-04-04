from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Signup


def login_user(request):
    print(request.POST)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            messages.success(request, ('با موفقیت وارد شدید'))
            return redirect('home')
        else:
            messages.success(request, ('خطا در ورود'))
            return render(request, 'account/login.html')
    else:
        return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('خارج شدید'))
    return redirect('home')


def signup_user(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')#['username']
            # password = form.cleaned_data.get('password')#['password']
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            messages.success(request, ('با موفقیت وارد شدید'))
            return redirect('login_user')
        else:
            messages.success(request, ('نشد که بیای'))
            return redirect('signup')
    else:
        return render(request, 'account/signup.html', {'form': form})
