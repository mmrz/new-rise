from .models import Category, Product, ProductPrice
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def category_view(request, category_slug):
    context_dict = {}
    category = Category.objects.get(cat_slug=category_slug)
    if category.parent is not None:
        context_dict = {}
        context_dict['categories'] = Category.objects.filter(parent=None)
        return render(request, 'home.html', context=context_dict)
    else:
        context_dict['categories'] = Category.objects.filter(parent=None)
        context_dict['category'] = category
        return render(request, 'category.html', context=context_dict)


def cataloge_view(request, category_slug, subcategory_slug):
    context_dict = {}
    category = Category.objects.get(cat_slug=category_slug)
    subcategory = Category.objects.get(cat_slug=subcategory_slug)
    context_dict['category'] = category
    context_dict['subcategory'] = subcategory

    context_dict['categories'] = Category.objects.filter(parent=None)
    product_list = Product.objects.prefetch_related('product_price').filter(category=subcategory)
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 1)
    try:
        context_dict['products'] = paginator.page(page)
    except PageNotAnInteger:
        context_dict['products'] = paginator.page(1)
    except EmptyPage:
        context_dict['products'] = paginator.page(paginator.num_pages)

    return render(request, 'catalog.html', context=context_dict)


def product_view(request, category_slug, subcategory_slug, product_id):
    context_dict = {}
    category = Category.objects.get(cat_slug=category_slug)
    subcategory = Category.objects.get(cat_slug=subcategory_slug)
    product = Product.objects.filter(id=product_id)
    context_dict['category'] = category
    context_dict['subcategory'] = subcategory
    context_dict['product'] = product
    context_dict['categories'] = Category.objects.filter(parent=None)
    return render(request, 'product.html', context=context_dict, )





