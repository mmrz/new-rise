from django import views
from users.models import User, Subscriptions
from django.shortcuts import render, get_object_or_404
from product.models import Category


def home(request):
    context_dict = {}
    context_dict['categories'] = Category.objects.filter(parent=None)
    return render(request, 'home.html', context=context_dict)
# Create your views here.
