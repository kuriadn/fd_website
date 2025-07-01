# pages/views.py

from django.shortcuts import render
from django.db.models import Q
from .models import HomePage, AboutPage, TeamMember
from services.models import Service
from portfolio.models import Portfolio
from blog.models import BlogPost

def home(request):
    """Homepage view with dynamic content"""
    
    # Get homepage content
    try:
        homepage = HomePage.objects.filter(is_active=True).first()
    except HomePage.DoesNotExist:
        homepage = None
    
    # Featured services (top 3)
    featured_services = Service.objects.filter(
        is_active=True, 
        is_featured=True
    ).order_by('order', 'name')[:3]
    
    # Featured portfolio items
    featured_portfolio = Portfolio.objects.filter(
        show_in_portfolio=True,
        featured=True
    ).order_by('-completion_date')[:3]
    
    # Latest blog posts
    latest_blog_posts = BlogPost.objects.filter(
        status='published'
    ).order_by('-published_at')[:3]
    
    # Stats - use from homepage model or defaults
    if homepage:
        stats = [
            {'number': homepage.stat_1_number, 'label': homepage.stat_1_label},
            {'number': homepage.stat_2_number, 'label': homepage.stat_2_label},
            {'number': homepage.stat_3_number, 'label': homepage.stat_3_label},
            {'number': homepage.stat_4_number, 'label': homepage.stat_4_label},
        ]
    else:
        stats = [
            {'number': '500+', 'label': 'SMEs Digitized'},
            {'number': '50+', 'label': 'SACCOs Served'},
            {'number': '98%', 'label': 'Client Satisfaction'},
            {'number': '24/7', 'label': 'Expert Support'},
        ]
    
    context = {
        'homepage': homepage,
        'featured_services': featured_services,
        'featured_portfolio': featured_portfolio,
        'latest_blog_posts': latest_blog_posts,
        'stats': stats,
    }
    
    return render(request, 'pages/home.html', context)

def about(request):
    """About page view"""
    
    # Get about page content
    try:
        about_page = AboutPage.objects.filter(is_active=True).first()
    except AboutPage.DoesNotExist:
        # Create default content if none exists
        about_page = AboutPage.objects.create(
            company_story="""At Fayvad Digital, we believe that technology should empower, not complicate. Founded with a vision to bridge the digital divide for Small and Medium Enterprises (SMEs) and SACCOs across Kenya, we've dedicated ourselves to providing accessible, affordable, and effective digital solutions.

Our journey began with a simple observation: many businesses struggle with digital transformation not because they lack vision, but because they lack the right partner. We set out to be that partner – one that understands the unique challenges of growing businesses and provides solutions that actually work.

Today, we're proud to have helped over 500 SMEs and 50+ SACCOs transform their operations, streamline their processes, and achieve sustainable growth through smart technology adoption.""",
            
            mission="To empower SMEs and SACCOs with smart, affordable digital solutions that drive sustainable business growth and operational excellence.",
            
            vision="To be the leading digital transformation partner for SMEs and SACCOs across East Africa, making advanced technology accessible to every growing business.",
            
            values="""• **Customer First**: Your success is our priority. We listen, understand, and deliver solutions tailored to your unique needs.
• **Quality Excellence**: We maintain the highest standards in every project, ensuring reliable, professional solutions.
• **Transparency**: Clear communication, honest pricing, and no hidden surprises – you know exactly what you're getting.
• **Continuous Innovation**: We stay ahead of technology trends to bring you the best and most current solutions.
• **Long-term Partnership**: We're not just service providers; we're your technology partners for the long haul."""
        )
    
    # Get team members
    team_members = TeamMember.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by('order', 'name')
    
    # Get some stats for about page
    service_count = Service.objects.filter(is_active=True).count()
    portfolio_count = Portfolio.objects.filter(show_in_portfolio=True).count()
    
    context = {
        'about_page': about_page,
        'team_members': team_members,
        'service_count': service_count,
        'portfolio_count': portfolio_count,
    }
    
    return render(request, 'pages/about.html', context)

def privacy_policy(request):
    """Privacy policy page"""
    return render(request, 'pages/privacy_policy.html')

def terms_of_service(request):
    """Terms of service page"""
    return render(request, 'pages/terms_of_service.html')