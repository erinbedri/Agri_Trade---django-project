from django.shortcuts import render


def show_homepage(request):
    return render(request, 'web/homepage.html')


def about(request):
    return render(request, 'web/about.html')


def imprint(request):
    return render(request, 'web/imprint.html')


def terms_and_conditions(request):
    return render(request, 'web/terms_and_conditions.html')


def data_protection(request):
    return render(request, 'web/data_protection.html')

