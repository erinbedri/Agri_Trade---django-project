from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from agri_trade.accounts.forms import CustomAuthenticationForm, CustomRegistrationForm, EditAccountForm, EditCompanyForm
from agri_trade.accounts.models import Company

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
                messages.success(request, f'You are now successfully logged in as {request.user.username}!')
                return redirect('web:homepage')
        else:
            messages.error(request, 'Login was unsuccessful! Fix the issues below.')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You are now successfully logged out from your account!')
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
            messages.error(request, 'Registration was unsuccessful! Fix the issues below.')
    else:
        form = CustomRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


@login_required
def account(request):
    company = get_object_or_404(Company, pk=request.user.id)

    context = {
        'company': company,
    }

    return render(request, 'accounts/account.html', context)


@login_required
def edit_account(request):
    company = get_object_or_404(Company, pk=request.user.id)

    if request.method == 'POST':
        account_form = EditAccountForm(request.POST, instance=request.user)
        company_form = EditCompanyForm(request.POST, instance=company)
        if account_form.is_valid() and company_form.is_valid():
            account_form.save()
            company_form.save()
            messages.success(request, 'Your account was updated successfully!')
            return redirect('accounts:account')
        else:
            messages.error(request, 'Edit was unsuccessful! Fix the issues below.')
    else:
        account_form = EditAccountForm(instance=request.user)
        company_form = EditCompanyForm(instance=company)

    context = {
        'account_form': account_form,
        'company_form': company_form,
    }

    return render(request, 'accounts/edit_account.html', context)

