from django.urls import path

from agri_trade.posts import views

urlpatterns = [
    path('all/', views.show_posts, name='show posts'),
    path('post/<int:pk>/', views.show_post, name='show post'),
    path('post/<int:pk>/comments/', views.show_comments, name='show comments'),
]