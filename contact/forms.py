# apps/contact/forms.py
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission 

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = [
            'name', 'email', 'phone', 'company', 
            'inquiry_type', 'subject', 'message', 
            'service_interest', 'budget_range'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+254-xxx-xxx-xxx'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your company name (optional)'
            }),
            'inquiry_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Brief subject line (optional)'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Tell us about your project or requirements...',
                'rows': 5
            }),
            'budget_range': forms.Select(
                choices=[
                    ('', 'Select budget range (optional)'),
                    ('under-50k', 'Under KSh 50,000'),
                    ('50k-100k', 'KSh 50,000 - 100,000'),
                    ('100k-250k', 'KSh 100,000 - 250,000'),
                    ('250k-500k', 'KSh 250,000 - 500,000'),
                    ('500k-1m', 'KSh 500,000 - 1,000,000'),
                    ('over-1m', 'Over KSh 1,000,000'),
                    ('discuss', 'Let\'s discuss'),
                ],
                attrs={'class': 'form-select'}
            ),
            'timeline': forms.Select(
                choices=[
                    ('', 'Select timeline (optional)'),
                    ('asap', 'ASAP'),
                    ('1-2-weeks', '1-2 weeks'),
                    ('2-4-weeks', '2-4 weeks'),
                    ('1-2-months', '1-2 months'),
                    ('3-6-months', '3-6 months'),
                    ('planning', 'Just planning ahead'),
                ],
                attrs={'class': 'form-select'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make certain fields required
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['inquiry_type'].required = True
        self.fields['message'].required = True
        
        # Pre-populate inquiry type if provided in URL
        if 'initial' in kwargs and 'inquiry_type' in kwargs['initial']:
            self.fields['inquiry_type'].initial = kwargs['initial']['inquiry_type']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Basic phone validation for Kenyan numbers
        phone = phone.replace(' ', '').replace('-', '')
        if not phone.startswith(('+254', '254', '0')):
            raise forms.ValidationError('Please enter a valid Kenyan phone number')
        return phone

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            # Send notification emails
            try:
                instance.send_notification_email()
                instance.send_confirmation_email()
            except Exception as e:
                # Log error but don't fail the form submission
                print(f"Email sending failed: {e}")
        return instance


class QuickContactForm(forms.Form):
    """Simplified contact form for quick inquiries"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'your@email.com'
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '+254-xxx-xxx-xxx'
        })
    )
    service = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Service you\'re interested in'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Brief message...',
            'rows': 3
        })
    )

    def send_email(self):
        """Send the quick contact email"""
        try:
            subject = f"Quick Contact: {self.cleaned_data['name']} - {self.cleaned_data['service']}"
            message = f"""
            New quick contact form submission:
            
            Name: {self.cleaned_data['name']}
            Email: {self.cleaned_data['email']}
            Phone: {self.cleaned_data['phone']}
            Service Interest: {self.cleaned_data['service']}
            
            Message:
            {self.cleaned_data['message']}
            """
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return True
        except Exception as e:
            print(f"Failed to send quick contact email: {e}")
            return False