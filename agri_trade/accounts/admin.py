from django.contrib import admin
from django.contrib.auth import get_user_model

from agri_trade.accounts.models import Company

UserModel = get_user_model()


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['account__username', 'name', 'vat', 'address', 'postcode', 'location', 'country']
    list_display = ('account', 'name', 'vat', 'address', 'postcode', 'location', 'country')
