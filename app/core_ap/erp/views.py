from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from core_ap.erp.models import Category, Product
"""importamos modelos creados en core_ap/erp"""


def myfirstview(request):
    data = {
        'name': 'Bryan',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def mysecondview(request):
    data = {
        'name': 'Bryan',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)


def vistaprueba(request):
    data = {
        'name': 'Bryan'
    }
    return JsonResponse(data)

