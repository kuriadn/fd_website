# contact/models.py

from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class ContactSubmission(models.Model):
    """Contact form submissions"""
    
    INQUIRY_TYPES = [
        ('general', 'General Inquiry'),
        ('quote', 'Service Quote'),
        ('support', 'Technical Support'),
        ('partnership', 'Partnership Opportunity'),
        ('other', 'Other'),
    ]
    
    # Contact Info
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    
    # Inquiry Details
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Service Interest (optional)
    service_interest = models.CharField(max_length=100, blank=True, help_text="Specific service they're interested in")
    budget_range = models.CharField(max_length=50, blank=True)
    
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)
    response_notes = models.TextField(blank=True, help_text="Internal notes about follow-up")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    def send_notification_email(self):
        """Send notification email to business"""
        message = f"""
New contact form submission from {self.name}

Contact Information:
Name: {self.name}
Email: {self.email}
Phone: {self.phone}
Company: {self.company}

Inquiry Details:
Type: {self.get_inquiry_type_display()}
Subject: {self.subject}
Service Interest: {self.service_interest}
Budget Range: {self.budget_range}

Message:
{self.message}

Submitted: {self.created_at}
        """
        
        try:
            send_mail(
                subject=f'New Contact: {self.subject}',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return True
        except Exception as e:
            print(f"Error sending notification email: {e}")
            return False
    
    def send_confirmation_email(self):
        """Send confirmation email to client"""
        confirmation_message = f"""
Hello {self.name},

Thank you for contacting Fayvad Digital! We have received your message and will get back to you within 24 hours.

Your Message:
Subject: {self.subject}
Message: {self.message}

If you have any urgent questions, please don't hesitate to call us at +254-769-069-640.

Best regards,
Fayvad Digital Team
services@digital.fayvad.com
+254-769-069-640

Grace House 3rd Floor Suite 10
Thika Town
www.digital.fayvad.com

---
This is an automated confirmation. Please do not reply to this email.
        """
        
        try:
            send_mail(
                subject='Thank you for contacting Fayvad Digital',
                message=confirmation_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email],
                fail_silently=True,
            )
            return True
        except Exception as e:
            print(f"Error sending confirmation email: {e}")
            return False

class Newsletter(models.Model):
    """Newsletter subscription"""
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return f"{self.email} - {self.name}"