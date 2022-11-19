from django.db.models import Q
from django.shortcuts import get_object_or_404

from agri_trade.accounts.models import Company
from agri_trade.marketplace.models import Product


def get_products_by_query(query):
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(cultivation_type__icontains=query) |
        Q(origin__icontains=query) |
        Q(location__icontains=query) |
        Q(variety__icontains=query) |
        Q(type__icontains=query) |
        Q(description__icontains=query) |
        Q(form__icontains=query) |
        Q(owner__username=query)) \
        .order_by('-created_on')
    return products


def get_favourites_by_query(user_id, query):
    favourites = get_object_or_404(Company, pk=user_id).favourites.filter(
        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(cultivation_type__icontains=query) |
        Q(origin__icontains=query) |
        Q(location__icontains=query) |
        Q(variety__icontains=query) |
        Q(type__icontains=query) |
        Q(description__icontains=query) |
        Q(form__icontains=query) |
        Q(owner__username=query)) \
        .order_by('-created_on')
    return favourites


def get_products_by_user_id(user_id):
    products = Product.objects.filter(owner_id=user_id)
    return products


def get_single_product(pk):
    product = get_object_or_404(Product, pk=pk)
    return product


def get_single_company(user_id):
    company = get_object_or_404(Company, pk=user_id)
    return company
