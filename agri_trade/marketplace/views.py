from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from agri_trade.marketplace.forms import AddProductForm, EditProductForm
from agri_trade.marketplace.models import Product


@login_required
def marketplace(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    products = Product.objects \
        .filter(
            Q(name__icontains=q) |
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


@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, 'Your produce was successfully added to the Marketplace!')
            return redirect('marketplace:marketplace')
        else:
            messages.error(request, "Your product couldn't be added. Please fix the form below!")
    else:
        form = AddProductForm()

    context = {
        'form': form,
    }

    return render(request, 'marketplace/add_product.html', context)


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product details were updates successfully!')
            return redirect('marketplace:marketplace')
        else:
            messages.error(request, 'Something went wrong! Please fix the form below.')
    else:
        form = EditProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'marketplace/edit_product.html', context)

