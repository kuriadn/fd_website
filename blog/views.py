# Create blog/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils import timezone
from .models import BlogPost, BlogCategory

def blog_list(request):
    """Display all published blog posts with filtering"""
    
    # Get filter parameters
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    # Base queryset - only published posts
    posts = BlogPost.objects.filter(
        status='published',
        published_at__lte=timezone.now()
    ).select_related('category', 'author')
    
    # Apply filters
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query) |
            Q(tags__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(posts, 9)  # 9 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories for filter dropdown
    categories = BlogCategory.objects.filter(is_active=True).annotate(
        post_count=Count('blogpost', filter=Q(blogpost__status='published'))
    )
    
    # Featured/Recent posts for sidebar
    featured_posts = BlogPost.objects.filter(
        status='published',
        is_featured=True,
        published_at__lte=timezone.now()
    )[:3]
    
    recent_posts = BlogPost.objects.filter(
        status='published',
        published_at__lte=timezone.now()
    ).exclude(id__in=[p.id for p in page_obj.object_list])[:5]
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'categories': categories,
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'current_category': category_slug,
        'search_query': search_query,
        'total_count': posts.count(),
    }
    
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    """Display individual blog post"""
    
    post = get_object_or_404(
        BlogPost.objects.select_related('category', 'author'),
        slug=slug,
        status='published',
        published_at__lte=timezone.now()
    )
    
    # Increment view count
    post.view_count += 1
    post.save(update_fields=['view_count'])
    
    # Get related posts (same category, excluding current)
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published',
        published_at__lte=timezone.now()
    ).exclude(id=post.id)[:3]
    
    # Get previous and next posts
    previous_post = BlogPost.objects.filter(
        status='published',
        published_at__lt=post.published_at
    ).order_by('-published_at').first()
    
    next_post = BlogPost.objects.filter(
        status='published',
        published_at__gt=post.published_at
    ).order_by('published_at').first()
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'previous_post': previous_post,
        'next_post': next_post,
        'absolute_image_url': request.build_absolute_uri(post.featured_image.url) if post.featured_image else None, 
    }
    
    return render(request, 'blog/blog_detail.html', context)

def category_detail(request, slug):
    """Display posts from a specific category"""
    
    category = get_object_or_404(BlogCategory, slug=slug, is_active=True)
    
    posts = BlogPost.objects.filter(
        category=category,
        status='published',
        published_at__lte=timezone.now()
    ).select_related('author')
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'posts': page_obj.object_list,
    }
    
    return render(request, 'blog/category_detail.html', context)

def featured_posts_context(request):
    """Context processor for featured posts (for homepage)"""
    
    featured_posts = BlogPost.objects.filter(
        status='published',
        is_featured=True,
        published_at__lte=timezone.now()
    )[:3]
    
    return {
        'featured_blog_posts': featured_posts
    }