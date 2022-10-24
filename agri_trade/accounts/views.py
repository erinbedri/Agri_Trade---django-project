from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect

from agri_trade.accounts.forms import CustomAuthenticationForm

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


def logout_user(request):
    context = {

    }

    return render(request, 'accounts/logout.html', context)


def register_user(request):
    context = {

    }

    return render(request, 'accounts/register.html', context)

