# apps/contact/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
import json
from .forms import ContactForm, QuickContactForm
from .models import ContactSubmission

class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')
    
    def get_initial(self):
        initial = super().get_initial()
        
        # Pre-populate form based on URL parameters
        inquiry_type = self.request.GET.get('type')
        service = self.request.GET.get('service')
        
        if inquiry_type:
            initial['inquiry_type'] = inquiry_type
            
        if service:
            initial['subject'] = f"Inquiry about {service}"
            
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Contact Fayvad Digital - Get Your Free Consultation"
        context['meta_description'] = "Contact Fayvad Digital for your digital transformation needs. Get expert advice on Odoo ERP, Zoho solutions, websites, and hosting."
        
        # Company contact information
        context['contact_info'] = {
            'address': 'Grace House 3rd Floor Suite 10, Kwame Nkuruma Road, Thika CBD',
            'phones': ['+254-769-069-640', '+254-727-399-208'],
            'email': 'services@digital.fayvad.com',
            'hours': 'Monday - Friday: 8:00 AM - 6:00 PM, Saturday: 9:00 AM - 2:00 PM'
        }
        
        # FAQ items
        context['faqs'] = [
            {
                'question': 'How quickly can you respond to my inquiry?',
                'answer': 'We respond to all inquiries within 2-6 hours during business hours. For urgent matters, call us directly.'
            },
            {
                'question': 'Do you offer free consultations?',
                'answer': 'Yes! We provide free initial consultations to understand your needs and recommend the best solutions.'
            },
            {
                'question': 'What information should I include in my message?',
                'answer': 'Tell us about your business, current challenges, and what you hope to achieve. The more details, the better we can help.'
            },
            {
                'question': 'Do you work with businesses outside Thika?',
                'answer': 'Absolutely! We serve clients across Kenya and can work remotely or arrange visits for larger projects.'
            }
        ]
        
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 
            'Thank you for contacting us! We\'ll get back to you within 2-6 hours during business hours.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            'Please correct the errors below and try again.'
        )
        return super().form_invalid(form)


def contact_success(request):
    """Success page after form submission"""
    return render(request, 'contact/success.html', {
        'page_title': 'Message Sent Successfully - Fayvad Digital'
    })


def quick_contact_ajax(request):
    """Handle AJAX quick contact form submissions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = QuickContactForm(data)
            
            if form.is_valid():
                # Send email
                if form.send_email():
                    return JsonResponse({
                        'success': True,
                        'message': 'Thank you! We\'ll contact you within 2 hours.'
                    })
                else:
                    return JsonResponse({
                        'success': False,
                        'message': 'Message sent but email notification failed. We\'ll still contact you!'
                    })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Please check your information and try again.',
                    'errors': form.errors
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid request format.'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })


# Simple function-based views for other contact pages
def contact_info(request):
    """Contact information page"""
    context = {
        'page_title': 'Contact Information - Fayvad Digital',
        'contact_details': {
            'address': {
                'line1': 'Grace House 3rd Floor Suite 10',
                'line2': 'Kwame Nkuruma Road',
                'city': 'Thika CBD',
                'country': 'Kenya'
            },
            'phones': [
                {'number': '+254-769-069-640', 'type': 'Primary'},
                {'number': '+254-727-399-208', 'type': 'Secondary'}
            ],
            'email': 'services@digital.fayvad.com',
            'business_hours': {
                'weekdays': 'Monday - Friday: 8:00 AM - 6:00 PM',
                'saturday': 'Saturday: 9:00 AM - 2:00 PM',
                'sunday': 'Sunday: Closed'
            }
        }
    }
    return render(request, 'contact/contact_info.html', context)