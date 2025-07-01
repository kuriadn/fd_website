# pages/models.py

from django.db import models

class HomePage(models.Model):
    """Homepage content management"""
    
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Empowering SMEs & SACCOs with Smart Digital Solutions")
    hero_subtitle = models.TextField(default="Transform your business with affordable, professional digital solutions. From websites to ERP systems, we're your trusted technology partner.")
    hero_cta_text = models.CharField(max_length=50, default="Get Free Consultation")
    hero_secondary_cta = models.CharField(max_length=50, default="View Our Services")
    
    # Stats Section
    stat_1_number = models.CharField(max_length=20, default="500+")
    stat_1_label = models.CharField(max_length=50, default="SMEs Digitized")
    
    stat_2_number = models.CharField(max_length=20, default="50+")
    stat_2_label = models.CharField(max_length=50, default="SACCOs Served")
    
    stat_3_number = models.CharField(max_length=20, default="98%")
    stat_3_label = models.CharField(max_length=50, default="Client Satisfaction")
    
    stat_4_number = models.CharField(max_length=20, default="24/7")
    stat_4_label = models.CharField(max_length=50, default="Expert Support")
    
    # About Section
    about_title = models.CharField(max_length=100, default="Why Choose Fayvad Digital?")
    about_content = models.TextField(default="We understand that every business is unique. That's why we take a personalized approach, listening carefully, designing solutions that fit your needs, and providing continuous support to ensure you succeed.")
    
    # Meta
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Content"
    
    def __str__(self):
        return "Homepage Content"

class AboutPage(models.Model):
    """About page content"""
    
    title = models.CharField(max_length=200, default="About Fayvad Digital")
    subtitle = models.CharField(max_length=300, default="Your trusted partner for digital transformation")
    
    # Company Info
    company_story = models.TextField(help_text="Main company story/description")
    mission = models.TextField(help_text="Company mission statement")
    vision = models.TextField(help_text="Company vision statement") 
    values = models.TextField(help_text="Company values (use line breaks for list)")
    
    # Team Section
    team_title = models.CharField(max_length=100, default="Our Expert Team")
    team_description = models.TextField(default="Meet the professionals dedicated to your digital success")
    
    # Services Overview
    services_title = models.CharField(max_length=100, default="What We Do")
    services_description = models.TextField(default="Comprehensive digital solutions for modern businesses")
    
    # Contact CTA
    cta_title = models.CharField(max_length=100, default="Ready to Transform Your Business?")
    cta_description = models.TextField(default="Let's discuss how we can help you achieve your digital goals")
    
    # Meta
    meta_description = models.CharField(max_length=160, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
    
    def __str__(self):
        return "About Page Content"

class TeamMember(models.Model):
    """Team member profiles"""
    
    ROLES = [
        ('director', 'Director'),
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('consultant', 'Consultant'),
        ('support', 'Support Specialist'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLES)
    title = models.CharField(max_length=100, help_text="Job title")
    bio = models.TextField(help_text="Professional biography")
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    
    # Contact Info
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    
    # Specializations
    specializations = models.TextField(blank=True, help_text="Areas of expertise (comma-separated)")
    
    # Meta
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_featured = models.BooleanField(default=True, help_text="Show on about page")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
    
    def __str__(self):
        return f"{self.name} - {self.title}"
    
    @property
    def specializations_list(self):
        if self.specializations:
            return [s.strip() for s in self.specializations.split(',')]
        return []