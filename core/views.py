from django.shortcuts import render, redirect
from item.models import *

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'main/index.html', {
        'items': items,
        'categories': categories,
    })

def contact(request):
    return render(request, 'main/contact.html')