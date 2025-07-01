# Add to your services/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Service, ServiceCategory

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'service_count', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    
    def service_count(self, obj):
        return obj.service_set.filter(is_active=True).count()
    service_count.short_description = 'Active Services'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price_display', 'billing_cycle', 
        'is_featured', 'is_active', 'created_at'
    ]
    list_filter = [
        'category', 'billing_cycle', 'is_featured', 
        'is_active', 'created_at'
    ]
    search_fields = ['name', 'description', 'features']
    list_editable = ['is_featured', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'short_description')
        }),
        ('Content', {
            'fields': ('description', 'features', 'benefits', 'requirements', 'process')
        }),
        ('Pricing', {
            'fields': ('price', 'setup_fee', 'billing_cycle')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        })
    )
    
    def price_display(self, obj):
        if obj.setup_fee:
            return format_html(
                'KES {} <small>+ {} setup</small>',
                f"{int(obj.price):,}",
                f"{int(obj.setup_fee):,}"
            )
        return format_html('KES {}', f"{int(obj.price):,}")

    price_display.short_description = 'Price'
    
    class Media:
        css = {
            'all': ('admin/css/services.css',)
        }