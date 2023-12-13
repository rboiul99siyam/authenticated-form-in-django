from django.shortcuts import render,redirect

from . forms import SingupForm,ChangeData
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm,SetPasswordForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def singup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Acount Create Successfully ')
            form.save()
    else:
        form = SingupForm()
    return render(request,'singup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request , data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = ChangeData(instance=request.user)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user ,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login')


