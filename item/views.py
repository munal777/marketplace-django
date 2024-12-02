from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def details(request, pk):
    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category = item.category).exclude(pk = pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'related_item': related_items,
        })