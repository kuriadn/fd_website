# services/models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class ServiceCategory(models.Model):
    """Service categories (Web Solutions, Business Systems, etc.)"""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class or emoji")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Service Categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:category', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Service(models.Model):
    """Individual services offered"""
    
    BILLING_CYCLES = [
        ('one_time', 'One Time'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('quarterly', 'Quarterly'),
    ]
    
    # Basic Info
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    description = models.TextField(help_text="Detailed service description")
    
    # Features & Benefits
    features = models.TextField(help_text="Service features (one per line)")
    benefits = models.TextField(blank=True, help_text="Key benefits for clients")
    requirements = models.TextField(blank=True, help_text="What client needs to provide")
    process = models.TextField(blank=True, help_text="Our process/methodology")
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    setup_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    billing_cycle = models.CharField(max_length=20, choices=BILLING_CYCLES, default='one_time')
    
    # Display Options
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    is_active = models.BooleanField(default=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})
    
    @property
    def features_list(self):
        """Return features as a list"""
        if self.features:
            return [f.strip() for f in self.features.split('\n') if f.strip()]
        return []
    
    @property
    def total_cost(self):
        """Calculate total first-time cost including setup fee"""
        total = self.price
        if self.setup_fee:
            total += self.setup_fee
        return total
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.meta_description:
            self.meta_description = self.short_description[:160]
        super().save(*args, **kwargs)