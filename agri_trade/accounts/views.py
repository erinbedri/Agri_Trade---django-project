from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from agri_trade.accounts.forms import CustomAuthenticationForm, CustomRegistrationForm

UserModel = get_user_model()


def login_user(request):
    if request.user.is_authenticated:
        return redirect('web:homepage')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('web:homepage')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('web:homepage')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('web:homepage')

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('web:homepage')
    else:
        form = CustomRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

