from django.contrib import admin

from agri_trade.marketplace.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'variety', 'type', 'form', 'size', 'cultivation_type', 'available_volume', 'price')
