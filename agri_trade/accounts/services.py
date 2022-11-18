from django.shortcuts import get_object_or_404

from agri_trade.accounts.models import Company


def get_single_company(user_id):
    company = get_object_or_404(Company, pk=user_id)
    return company
