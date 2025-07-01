# Add these models to your existing models.py file
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class PortfolioCategory(models.Model):
    """Categories for portfolio items (Web Development, ERP, CRM, etc.)"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Portfolio Categories"
    
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    """Portfolio/Case Study items"""
    
    SERVICE_TYPES = [
        ('website', 'Website Development'),
        ('odoo', 'Odoo ERP'),
        ('zoho', 'Zoho Solutions'),
        ('crm', 'CRM Implementation'),
        ('hosting', 'Hosting & Domain'),
        ('ecommerce', 'E-commerce'),
        ('custom', 'Custom Development'),
    ]
    
    PROJECT_STATUS = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=100)
    client_logo = models.ImageField(upload_to='portfolio/logos/', blank=True, null=True)
    
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolio_items')
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    
    # Project Details
    short_description = models.CharField(max_length=300, help_text="Brief description for cards/previews")
    description = models.TextField(help_text="Detailed project description")
    challenge = models.TextField(help_text="What challenge did this project solve?", blank=True)
    solution = models.TextField(help_text="How did we solve it?", blank=True)
    results = models.TextField(help_text="What were the outcomes/results?", blank=True)
    
    # Media
    featured_image = models.ImageField(upload_to='portfolio/featured/')
    gallery_images = models.JSONField(default=list, blank=True, help_text="List of additional image URLs")
    
    # Project Info
    project_url = models.URLField(blank=True, help_text="Live project URL")
    demo_url = models.URLField(blank=True, help_text="Demo or staging URL")
    completion_date = models.DateField()
    duration_months = models.PositiveIntegerField(help_text="Project duration in months")
    project_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Client Feedback
    client_testimonial = models.TextField(blank=True, help_text="Client testimonial/quote")
    client_rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)
    
    # Meta
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    show_in_portfolio = models.BooleanField(default=True)
    technologies_used = models.JSONField(default=list, help_text="List of technologies/tools used")
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-completion_date']
        verbose_name = "Portfolio Item"
        verbose_name_plural = "Portfolio Items"
    
    def __str__(self):
        return f"{self.title} - {self.client_name}"
    
    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'slug': self.slug})
    
    @property
    def primary_technology(self):
        """Returns the main technology used"""
        if self.technologies_used:
            return self.technologies_used[0]
        return self.get_service_type_display()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.client_name}-{self.title}")
        if not self.meta_description:
            self.meta_description = self.short_description[:160]
        super().save(*args, **kwargs)