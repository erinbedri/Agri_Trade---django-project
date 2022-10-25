from django.urls import path

from agri_trade.accounts import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.account, name='account'),
    path('account/edit', views.edit_account, name='edit account'),
]