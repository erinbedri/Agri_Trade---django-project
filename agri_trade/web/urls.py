from django.urls import path

from agri_trade.web import views

urlpatterns = [
    path('', views.show_homepage, name='homepage'),
]
