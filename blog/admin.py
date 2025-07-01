# blog/admin.py - Fixed to match actual model fields

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import BlogPost, BlogCategory

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'post_count']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    
    def post_count(self, obj):
        return obj.blogpost_set.filter(status='published').count()
    post_count.short_description = 'Published Posts'

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'category', 'status', 'is_featured', 
        'published_at', 'view_count', 'reading_time', 'thumbnail'
    ]
    list_filter = [
        'status', 'is_featured', 'category', 'created_at', 
        'published_at', 'author'
    ]
    search_fields = ['title', 'content', 'excerpt', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status', 'is_featured']
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at', 'is_featured')
        }),
        ('SEO & Meta', {
            'fields': ('meta_description', 'tags'),
            'classes': ('collapse',)
        }),
        ('Advanced', {
            'fields': ('view_count',),
            'classes': ('collapse',)
        })
    )
    
    readonly_fields = ['view_count', 'created_at', 'updated_at']
    
    def thumbnail(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.featured_image.url
            )
        return "No image"
    thumbnail.short_description = 'Image'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new post
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)