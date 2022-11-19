from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from agri_trade.marketplace.forms import AddProductForm, EditProductForm, DeleteProductForm
from agri_trade.marketplace.models import Product

from agri_trade.marketplace import services as marketplace_services

UserModel = get_user_model()

PRODUCTS_PER_PAGE = 10


@login_required
def marketplace(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    products = marketplace_services.get_products_by_query(query=q)
    products_count = products.count()

    categories = sorted({product.category for product in Product.objects.all()})
    cultivation_types = sorted({product.cultivation_type for product in Product.objects.all()})
    origins = sorted({product.origin.name for product in Product.objects.all()})
    locations = sorted({product.location.name for product in Product.objects.all()})

    paginator = Paginator(products, PRODUCTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'cultivation_types': cultivation_types,
        'origins': origins,
        'locations': locations,
        'page_obj': page_obj,
        'query': q,
        'products_count': products_count,
    }

    return render(request, 'marketplace/marketplace.html', context)


@login_required
def product_details(request, pk):
    product = marketplace_services.get_single_product(pk=pk)
    user_company = marketplace_services.get_single_company(user_id=request.user.id)

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
    product = marketplace_services.get_single_product(pk=pk)

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
    product = marketplace_services.get_single_product(pk=pk)

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
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    favourites = marketplace_services.get_favourites_by_query(user_id=request.user.id, query=q)
    favourites_count = favourites.count()

    categories = sorted({favourite.category for favourite in favourites})
    cultivation_types = sorted({favourite.cultivation_type for favourite in favourites})
    origins = sorted({favourite.origin.name for favourite in favourites})
    locations = sorted({favourite.location.name for favourite in favourites})

    paginator = Paginator(favourites, PRODUCTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
    user_company = marketplace_services.get_single_company(user_id=request.user.id)
    product = marketplace_services.get_single_product(pk=pk)
    is_in_favourites = False

    if user_company.favourites.filter(id=product.id).exists():
        user_company.favourites.remove(product)
        is_in_favourites = False
    else:
        user_company.favourites.add(product)
        is_in_favourites = True

    return HttpResponseRedirect(reverse('marketplace:product details', args=[str(pk)]))


@login_required
def show_my_products(request):
    my_products = marketplace_services.get_products_by_user_id(user_id=request.user.id)
    my_products_count = my_products.count()

    paginator = Paginator(my_products, PRODUCTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'my_products': page_obj,
        'page_obj': page_obj,
        'my_products_count': my_products_count,
    }

    return render(request, 'marketplace/show_my_products.html', context)
