from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name= 'items'),
    path('<int:pk>/', views.details, name='detail'),
    path('new/', views.newitem, name='new'),
    path('<int:pk>/delete', views.delete_item, name= 'delete'),
    path('edit/<int:pk>/', views.edititem, name= 'edit')
]