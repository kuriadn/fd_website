# Create services/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Service, ServiceCategory

def service_list(request):
    """Display all services with filtering"""
    
    # Get filter parameters
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    # Base queryset
    services = Service.objects.filter(is_active=True).select_related('category')
    
    # Apply filters
    if category_slug:
        services = services.filter(category__slug=category_slug)
    
    if search_query:
        services = services.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(features__icontains=search_query)
        )
    
    # Get categories for filter dropdown
    categories = ServiceCategory.objects.filter(is_active=True)
    
    # Featured services for homepage/top display
    featured_services = services.filter(is_featured=True)[:3]
    
    context = {
        'services': services,
        'categories': categories,
        'featured_services': featured_services,
        'current_category': category_slug,
        'search_query': search_query,
        'total_count': services.count(),
    }
    
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    """Display individual service details"""
    
    service = get_object_or_404(
        Service.objects.select_related('category'),
        slug=slug,
        is_active=True
    )
    
    # Get related services (same category, excluding current)
    related_services = Service.objects.filter(
        category=service.category,
        is_active=True
    ).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    
    return render(request, 'services/service_detail.html', context)

def category_detail(request, slug):
    """Display services from a specific category"""
    
    category = get_object_or_404(ServiceCategory, slug=slug, is_active=True)
    
    services = Service.objects.filter(
        category=category,
        is_active=True
    )
    
    context = {
        'category': category,
        'services': services,
    }
    
    return render(request, 'services/category_detail.html', context)
   