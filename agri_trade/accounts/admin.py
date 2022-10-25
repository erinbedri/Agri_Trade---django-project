from django.contrib import admin

from agri_trade.accounts.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'vat', 'address', 'postcode', 'location', 'country')
