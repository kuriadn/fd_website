# apps/services/urls.py
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='list'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
    path('<slug:slug>/', views.service_detail, name='detail'),
]

