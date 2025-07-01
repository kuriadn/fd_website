# contact/urls.py
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='form'),
    path('success/', views.contact_success, name='success'),
    path('info/', views.contact_info, name='info'),
    path('quick-contact/', views.quick_contact_ajax, name='quick_contact_ajax'),
]