from django.contrib import admin

from agri_trade.marketplace.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'variety', 'cultivation_type', 'available_volume', 'price', 'created_on')
