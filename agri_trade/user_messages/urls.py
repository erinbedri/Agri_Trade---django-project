from django.urls import path

from agri_trade.user_messages import views

urlpatterns = [
    path('', views.show_messages, name='messages'),
    path('message/<int:pk>', views.show_message, name='message'),
    path('send-message/<int:pk>', views.send_message, name='send message')
]