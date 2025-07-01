# Create portfolio/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Portfolio, PortfolioCategory

def portfolio_list(request):
    """Display all portfolio items with filtering"""
    
    # Get filter parameters
    category_slug = request.GET.get('category')
    service_type = request.GET.get('service')
    search_query = request.GET.get('q')
    
    # Base queryset
    portfolios = Portfolio.objects.filter(show_in_portfolio=True)
    
    # Apply filters
    if category_slug:
        portfolios = portfolios.filter(category__slug=category_slug)
    
    if service_type:
        portfolios = portfolios.filter(service_type=service_type)
    
    if search_query:
        portfolios = portfolios.filter(
            Q(title__icontains=search_query) |
            Q(client_name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies_used__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(portfolios, 12)  # 12 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories and service types for filters
    categories = PortfolioCategory.objects.filter(is_active=True)
    service_types = Portfolio.SERVICE_TYPES
    
    context = {
        'page_obj': page_obj,
        'portfolios': page_obj.object_list,
        'categories': categories,
        'service_types': service_types,
        'current_category': category_slug,
        'current_service': service_type,
        'search_query': search_query,
        'total_count': portfolios.count(),
    }
    
    return render(request, 'portfolio/portfolio_list.html', context)

def portfolio_detail(request, slug):
    """Display individual portfolio item"""
    
    portfolio = get_object_or_404(
        Portfolio.objects.select_related('category'),
        slug=slug,
        show_in_portfolio=True
    )
    
    # Get related portfolio items (same service type, excluding current)
    related_portfolios = Portfolio.objects.filter(
        service_type=portfolio.service_type,
        show_in_portfolio=True
    ).exclude(id=portfolio.id)[:3]
    
    context = {
        'portfolio': portfolio,
        'related_portfolios': related_portfolios,
    }
    
    return render(request, 'portfolio/portfolio_detail.html', context)

def featured_portfolio(request):
    """Get featured portfolio items for homepage"""
    
    featured_items = Portfolio.objects.filter(
        featured=True,
        show_in_portfolio=True
    )[:6]  # Show 6 featured items
    
    return {
        'featured_portfolio': featured_items
    }