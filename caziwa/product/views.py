from .models import Category, Product, ProductPrice, Comment
from django.shortcuts import render, HttpResponse,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.forms import CommentForm
from django.utils import timezone
import datetime, json
from django.http import JsonResponse


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
    product = Product.objects.get(id=product_id)
    commnets = Comment.objects.filter(product=product).order_by('date').reverse()
    context_dict['proid'] = product_id
    context_dict['category'] = category
    context_dict['subcategory'] = subcategory
    context_dict['product'] = product
    context_dict['categories'] = Category.objects.filter(parent=None)
    context_dict['comments'] = commnets
    if request.method == 'POST' and request.is_ajax:
        form = CommentForm(request.POST)
        products = get_object_or_404(Product, pk=product_id)
        User = request.user
        if form.is_valid():
            cm_text = form.cleaned_data['cm_text']
            comment = Comment()
            comment.product = products
            comment.users = User
            comment.cm_text = cm_text
            comment.date = datetime.datetime.now()
            comment.save()
            # form.save()
            msg = "The operation has been received correctly."
            print(request.POST)

            return HttpResponse(msg)
        else:
            msg = "GET petitions are not allowed for this view."
            return HttpResponse(msg)
    else:
        form = CommentForm()
    context_dict['form'] = form

    return render(request, 'product.html', context=context_dict, )



