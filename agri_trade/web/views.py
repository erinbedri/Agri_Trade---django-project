from django.shortcuts import render


def show_homepage(request):
    context = {

    }

    return render(request, 'web/homepage.html', context)
