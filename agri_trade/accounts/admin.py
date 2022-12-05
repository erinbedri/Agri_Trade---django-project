from django.contrib import admin
from agri_trade.accounts.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['account__username', 'name', 'vat', 'address', 'postcode', 'location', 'country']
    list_filter = ('country', )
    list_display = ('account', 'name', 'vat', 'address', 'postcode', 'location', 'country')
