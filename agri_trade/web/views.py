from django.shortcuts import render
from django.views.generic import TemplateView


# def show_homepage(request):
#     return render(request, 'web/homepage.html')


# def about(request):
#     return render(request, 'web/about.html')
#
#
# def imprint(request):
#     return render(request, 'web/imprint.html')
#
#
# def terms_and_conditions(request):
#     return render(request, 'web/terms_and_conditions.html')
#
#
# def data_protection(request):
#     return render(request, 'web/data_protection.html')


class HomepageView(TemplateView):
    template_name = 'web/homepage.html'


class AboutPageView(TemplateView):
    template_name = 'web/about.html'


class ImprintPageView(TemplateView):
    template_name = 'web/imprint.html'


class TermsAndConditionsPageView(TemplateView):
    template_name = 'web/terms_and_conditions.html'


class DataProtectionPageView(TemplateView):
    template_name = 'web/data_protection.html'

