from django.urls import path

from agri_trade.user_messages import views

urlpatterns = [
    path('', views.messages, name='messages'),
    path('message/<int:pk>', views.message, name='message')
]