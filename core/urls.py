from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('contact/', views.contact, name= 'contact'),
    path('signup/', views.signup_page, name= 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html',authentication_form = LoginForm), name='login'),
]