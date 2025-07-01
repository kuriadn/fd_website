# services/management/commands/setup_services_data.py

from django.core.management.base import BaseCommand
from services.models import ServiceCategory, Service
from decimal import Decimal


class Command(BaseCommand):
    help = 'Creates service categories and loads starter services data for Fayvad Digital'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite existing data',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Setting up Fayvad Digital services data...\n')
        )

        # Create categories
        self.create_categories(force=options['force'])
        
        # Load services data
        self.load_services_data(force=options['force'])
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Services setup completed successfully!')
        )

    def create_categories(self, force=False):
        """Create service categories"""
        
        categories_data = [
            {
                'id': 1,
                'name': 'Business Management Systems',
                'slug': 'business-management-systems',
                'description': 'Complete ERP and business process automation solutions powered by Odoo CE v17',
                'icon': '🏢',
                'order': 1,
                'is_active': True
            },
            {
                'id': 2,
                'name': 'Email & Communication Solutions',
                'slug': 'email-communication-solutions',
                'description': 'Professional email services and communication tools for modern businesses',
                'icon': '📧',
                'order': 2,
                'is_active': True
            },
            {
                'id': 3,
                'name': 'Web & Domain Services',
                'slug': 'web-domain-services',
                'description': 'Professional websites, domain registration, and hosting solutions',
                'icon': '🌐',
                'order': 3,
                'is_active': True
            },
            {
                'id': 4,
                'name': 'Custom Development',
                'slug': 'custom-development',
                'description': 'Tailored software solutions built from the ground up to meet your specific needs',
                'icon': '⚙️',
                'order': 4,
                'is_active': True
            }
        ]

        # Create categories
        for cat_data in categories_data:
            category, created = ServiceCategory.objects.get_or_create(
                id=cat_data['id'],
                defaults=cat_data
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created category: {category.name}')
                )
            elif force:
                for key, value in cat_data.items():
                    if key != 'id':
                        setattr(category, key, value)
                category.save()
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Updated category: {category.name}')
                )

    def load_services_data(self, force=False):
        """Load services data"""
        
        services_data = [
            # Business Management Systems
            {
                'id': 1,
                'name': 'Odoo ERP Starter Package',
                'slug': 'odoo-erp-starter-package',
                'category_id': 1,
                'short_description': 'Complete Odoo v17 CE setup with essential modules for growing SMEs and SACCOs',
                'description': '''Transform your business operations with our comprehensive Odoo ERP Starter Package. Built on Odoo Community Edition v17, this solution provides everything you need to manage your business processes efficiently.

Perfect for SMEs and SACCOs looking to digitize their operations, this package includes setup, configuration, training, and ongoing support to ensure your success.''',
                'features': '''CRM & Sales Management
Financial Accounting & Reporting
Inventory & Stock Management
Purchase & Supplier Management
Project Management
Human Resources (HR)
Document Management
Multi-user Access Control
Custom Reporting & Dashboards
Mobile App Access
Data Import & Migration
Initial Training (8 hours)
30-day Support Included''',
                'benefits': '''Streamlined business processes
Improved data accuracy and reporting
Better customer relationship management
Efficient inventory control
Automated workflows
Real-time business insights
Scalable solution that grows with your business''',
                'requirements': '''Basic business process documentation
List of users and their roles
Existing data for migration (if applicable)
Internet connection for cloud hosting
Management commitment to change process''',
                'process': '''1. Discovery Session: Understanding your business needs
2. System Setup: Installing and configuring Odoo modules
3. Data Migration: Importing your existing business data
4. Customization: Tailoring workflows to your processes
5. User Training: Comprehensive training for your team
6. Go-Live Support: Ensuring smooth transition
7. Ongoing Support: 30-day support included''',
                'price': Decimal('75000.00'),
                'setup_fee': Decimal('25000.00'),
                'billing_cycle': 'one_time',
                'order': 1,
                'is_featured': True,
                'is_active': True,
                'meta_description': 'Complete Odoo ERP setup for SMEs. CRM, accounting, inventory management with training and support. Transform your business operations today.',
                'meta_keywords': 'Odoo ERP, business management, CRM, accounting software, inventory management, Kenya'
            },
            {
                'id': 2,
                'name': 'Odoo ERP Professional Package',
                'slug': 'odoo-erp-professional-package',
                'category_id': 1,
                'short_description': 'Advanced Odoo v17 CE solution with custom modules and integrations for established businesses',
                'description': '''Take your business to the next level with our Professional Odoo ERP Package. This comprehensive solution includes advanced modules, custom integrations, and specialized features tailored for established businesses.

Ideal for companies with complex workflows, multiple departments, or specific industry requirements. Includes extensive customization and premium support.''',
                'features': '''All Starter Package Features
Manufacturing & Production Planning
Advanced Accounting & Multi-currency
E-commerce Integration
Website Builder Integration
Custom Module Development
Third-party API Integrations
Advanced Reporting & Analytics
Multi-company Management
Custom Workflows & Automations
Extended Training (16 hours)
60-day Premium Support
Performance Optimization''',
                'benefits': '''Comprehensive business automation
Advanced reporting capabilities
Custom integrations with existing systems
Multi-location support
Enhanced productivity
Better decision-making tools
Competitive advantage through automation''',
                'requirements': '''Detailed business process documentation
Technical specifications for integrations
Existing system data and APIs
Dedicated project coordinator
3-month implementation timeline''',
                'process': '''1. Comprehensive Business Analysis (2 weeks)
2. System Architecture & Design (1 week)
3. Custom Development & Configuration (4-6 weeks)
4. Integration Development (2-3 weeks)
5. User Acceptance Testing (1 week)
6. Training & Documentation (1 week)
7. Go-Live & Optimization (1 week)
8. Post-Go-Live Support (60 days)''',
                'price': Decimal('150000.00'),
                'setup_fee': Decimal('50000.00'),
                'billing_cycle': 'one_time',
                'order': 2,
                'is_featured': True,
                'is_active': True,
                'meta_description': 'Advanced Odoo ERP with custom development and integrations. Perfect for established businesses needing comprehensive automation.',
                'meta_keywords': 'Advanced Odoo ERP, custom development, business automation, integrations, professional ERP'
            },
            {
                'id': 3,
                'name': 'Custom Web Portal with Odoo Backend',
                'slug': 'custom-web-portal-odoo-backend',
                'category_id': 1,
                'short_description': 'Customer-facing web portal powered by Odoo backend for seamless business operations',
                'description': '''Create a professional customer portal that seamlessly integrates with your Odoo backend. Perfect for businesses that need custom customer interfaces while maintaining powerful backend management.

This solution combines the flexibility of custom web development with the robust business logic of Odoo ERP, giving you the best of both worlds.''',
                'features': '''Custom-designed web portal
Odoo v17 CE backend integration
Customer account management
Online ordering/booking system
Real-time inventory display
Payment gateway integration
Customer support ticketing
Mobile-responsive design
SEO optimization
SSL security
User role management
API development for integrations''',
                'benefits': '''Professional customer experience
Seamless order processing
Real-time data synchronization
Reduced manual work
24/7 customer access
Improved customer satisfaction
Scalable architecture''',
                'requirements': '''Portal design requirements
Customer workflow specifications
Odoo backend setup (can be included)
Payment gateway preferences
Branding materials
Content for the portal''',
                'process': '''1. Requirements Gathering & Design (2 weeks)
2. Portal Development & Styling (3-4 weeks)
3. Odoo Backend Configuration (1-2 weeks)
4. Integration Development (2-3 weeks)
5. Testing & Quality Assurance (1 week)
6. Training & Documentation (1 week)
7. Deployment & Go-Live Support''',
                'price': Decimal('120000.00'),
                'setup_fee': Decimal('30000.00'),
                'billing_cycle': 'one_time',
                'order': 3,
                'is_featured': True,
                'is_active': True,
                'meta_description': 'Custom web portal with Odoo backend integration. Perfect customer-facing solution with powerful business management.',
                'meta_keywords': 'custom web portal, Odoo integration, customer portal, web development, business automation'
            },
            
            # Email & Communication Solutions
            {
                'id': 4,
                'name': 'Professional Email Setup (Zoho Mail)',
                'slug': 'professional-email-setup-zoho',
                'category_id': 2,
                'short_description': 'Complete professional email solution with custom domain and Zoho Mail integration',
                'description': '''Establish professional communication for your business with our comprehensive email setup service. We configure Zoho Mail with your custom domain for a complete professional email solution.

Includes domain configuration, security setup, mobile sync, and team training to ensure you get the most from your professional email system.''',
                'features': '''Custom domain email setup
Zoho Mail professional configuration
Email security (SPF, DKIM, DMARC)
Mobile device configuration
Email signature setup
Alias and group email creation
Calendar and contacts sync
Spam and virus protection
Email forwarding and rules
Admin panel training
User account setup (up to 10 users)
Basic troubleshooting guide''',
                'benefits': '''Professional business communication
Enhanced security and reliability
Seamless mobile synchronization
Improved team collaboration
Better email organization
Protection from spam and threats
24/7 email access''',
                'requirements': '''Domain name (we can register if needed)
List of email accounts needed
Access to domain DNS settings
Team member information
Mobile devices for configuration''',
                'process': '''1. Domain verification and DNS setup
2. Zoho Mail account creation and configuration
3. Security protocols implementation
4. Mobile device configuration
5. Team training session (2 hours)
6. Testing and quality assurance
7. Documentation handover''',
                'price': Decimal('15000.00'),
                'setup_fee': None,
                'billing_cycle': 'one_time',
                'order': 1,
                'is_featured': False,
                'is_active': True,
                'meta_description': 'Professional email setup with Zoho Mail and custom domain. Complete configuration, security, and training included.',
                'meta_keywords': 'professional email, Zoho Mail, custom domain email, business email setup, email security'
            },
            {
                'id': 5,
                'name': 'Email Migration & Upgrade Service',
                'slug': 'email-migration-upgrade-service',
                'category_id': 2,
                'short_description': 'Seamless migration from existing email systems to professional Zoho Mail solution',
                'description': '''Upgrade your existing email system to a professional Zoho Mail solution without losing any important data. Our migration service ensures a smooth transition with zero downtime.

Perfect for businesses currently using basic email providers or outdated systems who want to upgrade to a more professional and feature-rich solution.''',
                'features': '''Complete email data migration
Contact and calendar migration
Email folder structure preservation
Historical email preservation
Zero downtime migration
DNS transition management
Mobile reconfiguration
Team retraining
Email rule recreation
Security upgrade
Archive organization
Post-migration support (14 days)''',
                'benefits': '''No data loss during migration
Improved email functionality
Better security and reliability
Professional appearance
Enhanced collaboration tools
Reduced IT maintenance
Seamless user experience''',
                'requirements': '''Current email system access
Email export capabilities
User account listing
DNS management access
Migration timing preferences
Team availability for training''',
                'process': '''1. Current system assessment
2. Migration planning and scheduling
3. Data export and preparation
4. Zoho Mail setup and configuration
5. Gradual migration execution
6. DNS cutover and testing
7. Team training and support
8. Post-migration monitoring''',
                'price': Decimal('25000.00'),
                'setup_fee': None,
                'billing_cycle': 'one_time',
                'order': 2,
                'is_featured': False,
                'is_active': True,
                'meta_description': 'Seamless email migration to Zoho Mail. Zero downtime migration with complete data preservation and team training.',
                'meta_keywords': 'email migration, Zoho Mail migration, email upgrade, data migration, professional email'
            },
            
            # Web & Domain Services
            {
                'id': 6,
                'name': 'Professional Business Website',
                'slug': 'professional-business-website',
                'category_id': 3,
                'short_description': 'Custom business website with modern design, SEO optimization, and mobile responsiveness',
                'description': '''Establish a strong online presence with our professional business website service. We create modern, mobile-responsive websites that showcase your business and attract customers.

Includes custom design, content management system, SEO optimization, and training to manage your website content effectively.''',
                'features': '''Custom website design
Mobile-responsive layout
Content Management System (CMS)
SEO optimization
Contact forms and lead capture
Google Analytics integration
Social media integration
SSL certificate included
Fast loading optimization
Basic security measures
Content creation assistance
Website training (3 hours)
30-day support included''',
                'benefits': '''Professional online presence
Increased customer credibility
Better search engine visibility
Lead generation capabilities
Mobile-friendly experience
Easy content management
Improved business visibility''',
                'requirements': '''Business information and branding
High-quality images and content
Logo and brand guidelines
Domain name (can be provided)
Hosting preferences
Website goals and objectives''',
                'process': '''1. Discovery and planning session
2. Design concepts and approval
3. Content creation and organization
4. Website development and testing
5. SEO optimization and setup
6. Training and handover
7. Launch and post-launch support''',
                'price': Decimal('45000.00'),
                'setup_fee': Decimal('10000.00'),
                'billing_cycle': 'one_time',
                'order': 1,
                'is_featured': False,
                'is_active': True,
                'meta_description': 'Professional business website with custom design, SEO optimization, and mobile responsiveness. Establish your online presence.',
                'meta_keywords': 'business website, website design, mobile responsive, SEO optimization, professional website'
            },
            {
                'id': 7,
                'name': 'Domain Registration & Management',
                'slug': 'domain-registration-management',
                'category_id': 3,
                'short_description': 'Complete domain registration, DNS management, and ongoing domain administration services',
                'description': '''Secure your business identity online with our domain registration and management service. We handle everything from domain search and registration to ongoing DNS management and renewals.

Includes domain consulting to find the perfect domain name, registration with premium providers, and ongoing management to ensure your domain stays secure and functional.''',
                'features': '''Domain availability search
Domain registration (.com, .co.ke, etc.)
DNS management and configuration
Email routing setup
Subdomain creation
Domain forwarding
SSL certificate coordination
Renewal management
Domain security features
Technical support
Annual renewal reminders
Domain transfer assistance''',
                'benefits': '''Secure business identity online
Professional email addresses
Better brand recognition
SEO benefits
Domain security
Hassle-free management
Expert technical support''',
                'requirements': '''Business information for registration
Preferred domain names
DNS requirements
Email setup needs
Hosting provider information''',
                'process': '''1. Domain consultation and search
2. Registration and verification
3. DNS configuration and setup
4. Email routing configuration
5. Security features activation
6. Documentation and training
7. Ongoing monitoring and support''',
                'price': Decimal('5000.00'),
                'setup_fee': None,
                'billing_cycle': 'yearly',
                'order': 2,
                'is_featured': False,
                'is_active': True,
                'meta_description': 'Domain registration and management services. Secure your business identity online with expert DNS management.',
                'meta_keywords': 'domain registration, DNS management, domain names, web hosting, domain security'
            },
            
            # Custom Development
            {
                'id': 8,
                'name': 'Custom Software Development',
                'slug': 'custom-software-development',
                'category_id': 4,
                'short_description': 'Tailored software solutions built from scratch to meet your specific business requirements',
                'description': '''Get exactly what your business needs with our custom software development service. We build tailored solutions from the ground up, ensuring every feature aligns with your specific requirements and business processes.

Perfect for businesses with unique workflows or specific requirements that off-the-shelf solutions can't address. Includes thorough planning, development, testing, and ongoing support.''',
                'features': '''Detailed requirements analysis
Custom application architecture
Modern technology stack
Database design and optimization
User interface/experience design
API development and integrations
Comprehensive testing
Documentation and training
Deployment and configuration
Source code delivery
3-month warranty support
Performance optimization''',
                'benefits': '''Perfect fit for your business needs
Competitive advantage
Scalable and maintainable code
Full ownership of the solution
No licensing limitations
Tailored user experience
Long-term cost effectiveness''',
                'requirements': '''Detailed business requirements
Process documentation
User workflow specifications
Technical preferences
Integration requirements
Timeline and budget parameters
Dedicated project contact''',
                'process': '''1. Requirements analysis and documentation (2-3 weeks)
2. Technical architecture and planning (1-2 weeks)
3. UI/UX design and approval (2-3 weeks)
4. Development and implementation (6-12 weeks)
5. Testing and quality assurance (2-3 weeks)
6. User training and documentation (1-2 weeks)
7. Deployment and go-live support
8. Post-launch support and optimization''',
                'price': Decimal('200000.00'),
                'setup_fee': Decimal('50000.00'),
                'billing_cycle': 'one_time',
                'order': 1,
                'is_featured': True,
                'is_active': True,
                'meta_description': 'Custom software development tailored to your business needs. Full-stack solutions built from scratch with ongoing support.',
                'meta_keywords': 'custom software development, tailored solutions, business software, application development, custom programming'
            },
            {
                'id': 9,
                'name': 'System Integration & API Development',
                'slug': 'system-integration-api-development',
                'category_id': 4,
                'short_description': 'Connect your existing systems with custom APIs and integrations for seamless data flow',
                'description': '''Break down data silos and create seamless workflows with our system integration and API development service. We connect your existing systems to enable automatic data synchronization and streamlined processes.

Ideal for businesses using multiple software systems that need to work together more effectively. Includes API development, data mapping, and ongoing integration support.''',
                'features': '''API development and documentation
System connectivity analysis
Data mapping and transformation
Real-time synchronization
Custom middleware development
Error handling and logging
Security implementation
Performance optimization
Integration testing
Technical documentation
Support and maintenance
Scalability planning''',
                'benefits': '''Eliminated manual data entry
Improved data accuracy
Streamlined workflows
Better business insights
Reduced operational costs
Enhanced productivity
Future-proof connectivity''',
                'requirements': '''Existing systems documentation
API specifications (if available)
Data flow requirements
Security requirements
Integration scope definition
Technical team coordination''',
                'process': '''1. Systems analysis and mapping (1-2 weeks)
2. Integration architecture design (1 week)
3. API development and testing (3-6 weeks)
4. Data mapping and transformation (2-3 weeks)
5. Security implementation (1-2 weeks)
6. Integration testing and validation (1-2 weeks)
7. Documentation and training
8. Deployment and monitoring setup''',
                'price': Decimal('80000.00'),
                'setup_fee': Decimal('20000.00'),
                'billing_cycle': 'one_time',
                'order': 2,
                'is_featured': False,
                'is_active': True,
                'meta_description': 'System integration and API development services. Connect your systems for seamless data flow and automated workflows.',
                'meta_keywords': 'system integration, API development, data integration, workflow automation, business connectivity'
            }
        ]

        # Create services
        created_count = 0
        updated_count = 0
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                id=service_data['id'],
                defaults=service_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created service: {service.name[:50]}...')
                )
            elif force:
                for key, value in service_data.items():
                    if key != 'id':
                        setattr(service, key, value)
                service.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Updated service: {service.name[:50]}...')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n📊 Services summary: {created_count} created, {updated_count} updated')
        )