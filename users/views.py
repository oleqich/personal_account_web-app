from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, ChangeUserForm
from django.views import View

def home(request):
    return render(request, 'users/index.html')

def edit_profile(request):
    form = CreateUserForm(initial={
        'username':request.user.username,
        'email':request.user.email,
        'bio':request.user.bio,

    })
    if request.method == 'POST':
        form = ChangeUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return render(request, 'users/edit.html', {'form':form})
    else:
        return render(request, 'users/edit.html', {'form':form,})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users')
        
    else:
        return render(request, 'users/signin.html')

def logout_user(request):
    logout(request)      
    return redirect(home)

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return render(request, 'users/signup.html', {'form':form})
    else:
        return render(request, 'users/signup.html', {'form':form,})