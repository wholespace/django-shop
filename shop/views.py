from . models import Category
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name':'Wazed'})


def product_list(request):

    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'productList.html', context)