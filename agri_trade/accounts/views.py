from django.shortcuts import render


def login(request):
    context = {

    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    context = {

    }

    return render(request, 'accounts/logout.html', context)


def register(request):
    context = {

    }

    return render(request, 'accounts/register.html', context)

