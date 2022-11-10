from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from agri_trade.accounts.models import Company
from agri_trade.marketplace.forms import AddProductForm, EditProductForm, DeleteProductForm
from agri_trade.marketplace.models import Product

UserModel = get_user_model()


@login_required
def marketplace(request):
    products_per_page = 10

    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    products = Product.objects.filter(
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

    categories = sorted({product.category for product in Product.objects.all()})
    cultivation_types = sorted({product.cultivation_type for product in Product.objects.all()})
    origins = sorted({product.origin.name for product in Product.objects.all()})
    locations = sorted({product.location.name for product in Product.objects.all()})

    paginator = Paginator(products, products_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'cultivation_types': cultivation_types,
        'origins': origins,
        'locations': locations,
        'page_obj': page_obj,
        'query': q,
        'products_count': len(products),
    }

    return render(request, 'marketplace/marketplace.html', context)


@login_required
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user_company = get_object_or_404(Company, pk=request.user.id)

    is_in_favourites = False
    if user_company.favourites.filter(id=product.id).exists():
        is_in_favourites = True

    context = {
        'product': product,
        'is_in_favourites': is_in_favourites,
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

    if request.user != product.owner:
        return redirect('marketplace:marketplace')

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


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user != product.owner:
        return redirect('marketplace:marketplace')

    if request.method == 'POST':
        form = DeleteProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if product.image:
                image = product.image
                image.delete()
            product.delete()
            return redirect('marketplace:marketplace')
    else:
        form = DeleteProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'marketplace/delete_product.html', context)


@login_required
def show_favourites(request):
    favourites_per_page = 10

    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    favourites = get_object_or_404(Company, pk=request.user.id).favourites.filter(
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

    categories = sorted({favourite.category for favourite in favourites})
    cultivation_types = sorted({favourite.cultivation_type for favourite in favourites})
    origins = sorted({favourite.origin.name for favourite in favourites})
    locations = sorted({favourite.location.name for favourite in favourites})

    paginator = Paginator(favourites, favourites_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    favourites_count = favourites.count()

    context = {
        'page_obj': page_obj,
        'favourites_count': favourites_count,
        'categories': categories,
        'cultivation_types': cultivation_types,
        'origins': origins,
        'locations': locations,
        'query': q,
    }

    return render(request, 'marketplace/show_favourites.html', context)


@login_required
def add_product_to_favourites(request, pk):
    user_company = get_object_or_404(Company, pk=request.user.id)
    product = get_object_or_404(Product, pk=pk)
    is_in_favourites = False

    if user_company.favourites.filter(id=product.id).exists():
        user_company.favourites.remove(product)
        is_in_favourites = False
    else:
        user_company.favourites.add(product)
        is_in_favourites = True

    return HttpResponseRedirect(reverse('marketplace:product details', args=[str(pk)]))
