from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item
from django.http import HttpResponse
@login_required
def dashboard(request):
    items = Item.objects.filter(created_by = request.user)

    return render(request, 'book/index.html', {
        'items': items,
    })
