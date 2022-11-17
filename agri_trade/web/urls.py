from django.urls import path

from agri_trade.web import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('imprint/', views.ImprintPageView.as_view(), name='imprint'),
    path('terms-and-conditions/', views.TermsAndConditionsPageView.as_view(), name='terms and conditions'),
    path('data-protection/', views.DataProtectionPageView.as_view(), name='data protection'),
]
