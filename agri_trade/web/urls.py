from django.urls import path

from agri_trade.web import views

urlpatterns = [
    path('', views.show_homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('imprint/', views.imprint, name='imprint'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms and conditions'),
    path('data-protection/', views.data_protection, name='data protection'),
]
