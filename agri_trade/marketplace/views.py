from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from agri_trade.marketplace.models import Product


@login_required
def marketplace(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    products = Product.objects \
        .filter(
            Q(category__icontains=q) |
            Q(cultivation_type__icontains=q) |
            Q(origin__icontains=q) |
            Q(location__icontains=q) |
            Q(variety__icontains=q) |
            Q(type__icontains=q) |
            Q(description__icontains=q) |
            Q(form__icontains=q) |
            Q(owner__username=q)) \
        .order_by('-created_on')

    categories = {product.category for product in Product.objects.all()}
    cultivation_types = {product.cultivation_type for product in Product.objects.all()}
    origins = {product.origin for product in Product.objects.all()}
    locations = {product.location for product in Product.objects.all()}

    context = {
        'products': products,
        'categories': categories,
        'cultivation_types': cultivation_types,
        'origins': origins,
        'locations': locations,
    }

    return render(request, 'marketplace/marketplace.html', context)


@login_required
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'marketplace/product_details.html', context)

