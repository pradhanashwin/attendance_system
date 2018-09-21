from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout, update_session_auth_hash)

from .forms import LoginForm, RegisterForm, ChangePasswordForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "attendance/home.html")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return render(request, 'custom_registration/login.html', {'form': form})

    else:
        form = LoginForm()

    return render(request, 'custom_registration/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'custom_registration/logged_out.html')


def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                    login(request, user)
                    return render(request, "attendance/home.html")
                else:
                    context = {'form': form,
                               'error_message': 'Password Dont Match'}
            else:
                return HttpResponse("Disabled Account")
        else:
            return render(request, 'custom_registration/register.html', {'form': form})

    else:

        form = LoginForm()
        context = {'form': form,
                   }

    return render(request, 'custom_registration/register.html', context)

