# Add to your admin.py file

from django.contrib import admin
from django.utils.html import format_html
from .models import Portfolio, PortfolioCategory

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'is_active', 'portfolio_count']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    
    def portfolio_count(self, obj):
        return obj.portfolio_items.count()
    portfolio_count.short_description = 'Items'

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'client_name', 'service_type', 'status', 
        'featured', 'completion_date', 'client_rating', 'thumbnail'
    ]
    list_filter = [
        'service_type', 'status', 'featured', 'category', 
        'completion_date', 'client_rating'
    ]
    search_fields = ['title', 'client_name', 'description']
    list_editable = ['featured', 'status']
    prepopulated_fields = {'slug': ('title', 'client_name')}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'client_name', 'client_logo', 'category', 'service_type')
        }),
        ('Project Description', {
            'fields': ('short_description', 'description', 'challenge', 'solution', 'results')
        }),
        ('Media', {
            'fields': ('featured_image', 'gallery_images')
        }),
        ('Project Details', {
            'fields': ('project_url', 'demo_url', 'completion_date', 'duration_months', 'project_cost', 'technologies_used')
        }),
        ('Client Feedback', {
            'fields': ('client_testimonial', 'client_rating')
        }),
        ('Settings', {
            'fields': ('status', 'featured', 'show_in_portfolio')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        })
    )
    
    def thumbnail(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.featured_image.url
            )
        return "No image"
    thumbnail.short_description = 'Image'
    
    class Media:
        css = {
            'all': ('admin/css/portfolio.css',)
        }