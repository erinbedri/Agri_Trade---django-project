from django.urls import path

from agri_trade.marketplace import views

urlpatterns = [
    path('', views.marketplace, name='marketplace'),
    path('product-add/', views.add_product, name='add product'),
    path('product-details/<int:pk>', views.product_details, name='product details'),
    path('product-edit/<int:pk>', views.edit_product, name='edit product'),
    path('product-delete/<int:pk>', views.delete_product, name='delete product'),
    path('favourites/', views.show_favourites, name='show favourites'),
]
