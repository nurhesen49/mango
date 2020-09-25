from django.shortcuts import render
from .forms import UserForm, UserExtra

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html', {})

def registration(request):
    registered = False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        user_extra=UserExtra(request.POST)
        if user_form.is_valid() and user_extra.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            extra=user_extra.save(commit=False)
            extra.user=user
            extra.save()
            registered=True
        else:
            return HttpResponse('sorry cannot validate')


    return render(request, 'registration.html', {'uf':UserForm, 'ux': UserExtra, 'registered':registered})
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('mangoapp:home'))

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mangoapp:home'))
            else:
                return HttpResponse('User not active')
        else:
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            return HttpResponse('User not found')
    return render(request, 'login.html', {})
