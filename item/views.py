from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.db.models import Q

# Create your views here.
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    item = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if category_id:
        item = item.filter(category_id = category_id)

    if query:
        item = item.filter(Q(name__icontains = query) | Q(category__name__icontains = query))


    return render(request, 'item/item.html', {
        'item':item,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def details(request, pk):
    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category = item.category).exclude(pk = pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'related_item': related_items,
        })

def delete_item(request, pk):
    item = get_object_or_404(Item, pk = pk, created_by = request.user)
    item.delete()

    return redirect('dashboard:dashboard')

@login_required
def newitem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('core:home')
    else:
        form = NewItemForm()

    return render(request, 'item/add-item.html', {
        'form': form,
        'title': 'New item'
    })

@login_required
def edititem(request, pk):
    item = get_object_or_404(Item, pk =pk)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()
            return redirect('core:home')
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/edit-item.html', {
        'form': form,
        'title': 'Edit item'
    })                                                                                                                                                                                                       