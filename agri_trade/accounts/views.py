from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from agri_trade.accounts.forms import CustomAuthenticationForm, CustomRegistrationForm, EditAccountForm, EditCompanyForm
from agri_trade.accounts import services as accounts_services

UserModel = get_user_model()

LOGIN_SUCCESS_MESSAGE = 'You are now successfully logged in!'
LOGIN_ERROR_MESSAGE = 'Login was unsuccessful! Fix the issues below.'

LOGOUT_SUCCESS_MESSAGE = 'You are now successfully logged out from your account!'

REGISTRATION_SUCCESS_MESSAGE = 'Your registration was successful! Please log in!'
REGISTRATION_ERROR_MESSAGE = 'Registration was unsuccessful! Fix the issues below.'

EDIT_SUCCESS_MESSAGE = 'Your account was updated successfully!'
EDIT_ERROR_MESSAGE = 'Edit was unsuccessful! Fix the issues below.'

SESSION_EXPIRATION_TIME_IN_SECONDS = 0


def login_user(request):
    if request.user.is_authenticated:
        return redirect('web:homepage')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(SESSION_EXPIRATION_TIME_IN_SECONDS)
                messages.success(request, LOGIN_SUCCESS_MESSAGE)
                return redirect('marketplace:marketplace')
        else:
            messages.error(request, LOGIN_ERROR_MESSAGE)
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, LOGOUT_SUCCESS_MESSAGE)
    return redirect('web:homepage')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('web:homepage')

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, REGISTRATION_SUCCESS_MESSAGE)
            return redirect('accounts:login')
        else:
            messages.error(request, REGISTRATION_ERROR_MESSAGE)
    else:
        form = CustomRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


@login_required
def account(request):
    company = accounts_services.get_single_company(user_id=request.user.id)

    context = {
        'company': company,
    }

    return render(request, 'accounts/account.html', context)


@login_required
def edit_account(request):
    company = accounts_services.get_single_company(user_id=request.user.id)

    if request.method == 'POST':
        account_form = EditAccountForm(request.POST, instance=request.user)
        company_form = EditCompanyForm(request.POST, instance=company)
        if account_form.is_valid() and company_form.is_valid():
            account_form.save()
            company_form.save()
            messages.success(request, EDIT_SUCCESS_MESSAGE)
            return redirect('accounts:account')
        else:
            messages.error(request, EDIT_ERROR_MESSAGE)
    else:
        account_form = EditAccountForm(instance=request.user)
        company_form = EditCompanyForm(instance=company)

    context = {
        'account_form': account_form,
        'company_form': company_form,
    }

    return render(request, 'accounts/edit_account.html', context)

