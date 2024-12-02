from django.shortcuts import render, redirect
from item.models import *
from .forms import SignupForm

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

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('core:login')
    else:
        form = SignupForm()


    return render(request, 'main/signup.html', {
        'form': form,
    })



# def login_page(request):
#     if request.method == 'POST':
#           form = LoginForm(request.POST)

#           if form.is_valid():
#                user = form.get_user()
#                if user:
#                     login(request, user)
#                     return redirect('core:home')

#     else:
#           form = LoginForm()
     
#     return render(request, 'main/login.html', {'form': form}) 