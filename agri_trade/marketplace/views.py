from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from agri_trade.marketplace.models import Product


@login_required
def marketplace(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'marketplace/marketplace.html', context)


@login_required
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'marketplace/product_details.html', context)

