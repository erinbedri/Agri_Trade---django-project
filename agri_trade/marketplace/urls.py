from django.urls import path

from agri_trade.marketplace import views

urlpatterns = [
    path('', views.marketplace, name='marketplace'),
    path('product-details/<int:pk>', views.product_details, name='product details'),
]
