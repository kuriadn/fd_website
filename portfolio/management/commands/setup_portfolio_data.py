# portfolio/management/commands/setup_portfolio_data.py

from django.core.management.base import BaseCommand
from portfolio.models import PortfolioCategory, Portfolio
from django.utils import timezone
from datetime import date
from decimal import Decimal


class Command(BaseCommand):
    help = 'Creates portfolio categories and loads starter portfolio data for Fayvad Digital'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite existing data',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Setting up Fayvad Digital portfolio data...\n')
        )

        # Create categories
        self.create_categories(force=options['force'])
        
        # Load portfolio data
        self.load_portfolio_data(force=options['force'])
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Portfolio setup completed successfully!')
        )

    def create_categories(self, force=False):
        """Create portfolio categories"""
        
        categories_data = [
            {
                'id': 1,
                'name': 'Web Development',
                'slug': 'web-development',
                'description': 'Professional websites and web applications built for various industries',
                'order': 1,
                'is_active': True
            },
            {
                'id': 2,
                'name': 'ERP & Business Solutions',
                'slug': 'erp-business-solutions',
                'description': 'Enterprise Resource Planning systems and business automation solutions',
                'order': 2,
                'is_active': True
            },
            {
                'id': 3,
                'name': 'Non-Profit Solutions',
                'slug': 'non-profit-solutions',
                'description': 'Specialized solutions for charitable organizations and children\'s homes',
                'order': 3,
                'is_active': True
            },
            {
                'id': 4,
                'name': 'Domain & Infrastructure',
                'slug': 'domain-infrastructure',
                'description': 'Domain management, hosting solutions, and digital infrastructure',
                'order': 4,
                'is_active': True
            },
            {
                'id': 5,
                'name': 'Training & Consulting',
                'slug': 'training-consulting',
                'description': 'Business process automation training and consulting services',
                'order': 5,
                'is_active': True
            }
        ]

        for cat_data in categories_data:
            category, created = PortfolioCategory.objects.get_or_create(
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

    def load_portfolio_data(self, force=False):
        """Load portfolio projects data based on actual model fields"""
        
        portfolio_data = [
            # Web Development Projects - Fayvad Brand Sites
            {
                'id': 1,
                'title': 'Fayvad Digital Corporate Website',
                'slug': 'fayvad-digital-corporate-website',
                'client_name': 'Fayvad Digital',
                'category_id': 1,
                'service_type': 'website',
                'short_description': 'Modern corporate website showcasing digital services for SMEs and SACCOs',
                'description': '''Professional corporate website for Fayvad Digital, featuring modern design, comprehensive service showcases, and client-focused messaging. Built with Django framework for robust content management and optimal user experience.

The website serves as the primary digital presence for the company, effectively communicating our value proposition to potential SME and SACCO clients through strategic content placement and conversion-optimized design.

Key features include dynamic service portfolio display, integrated blog functionality for thought leadership content, contact forms with automated lead routing, and mobile-responsive design ensuring accessibility across all devices.''',
                'challenge': '''Fayvad Digital needed a professional online presence that would effectively communicate their expertise in business automation and digital transformation to SMEs and SACCOs while establishing credibility in the competitive digital services market.''',
                'solution': '''Designed and developed a modern, responsive website using Django framework with custom CMS functionality. Implemented SEO optimization, performance optimization, and integrated contact systems to maximize lead generation and client engagement.''',
                'results': '''Successfully launched the corporate website which now serves as the central hub for client acquisition. The site features comprehensive service information, client testimonials, and thought leadership content that positions Fayvad Digital as a trusted partner for business digitization.''',
                'project_url': 'https://digital.fayvad.com',
                'demo_url': '',
                'completion_date': date(2024, 12, 1),
                'duration_months': 2,
                'project_cost': Decimal('150000.00'),
                'client_testimonial': 'The website perfectly represents our brand and has significantly improved our professional image. It effectively communicates our services to potential clients.',
                'client_rating': 5,
                'status': 'completed',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Django', 'Python', 'PostgreSQL', 'TailwindCSS', 'Alpine.js', 'Docker'],
                'meta_description': 'Corporate website for Fayvad Digital - professional digital services for SMEs and SACCOs',
                'meta_keywords': 'Fayvad Digital, corporate website, Django development, SME services, SACCO solutions'
            },
            {
                'id': 2,
                'title': 'Fayvad Brand Creative Portfolio',
                'slug': 'fayvad-brand-creative-portfolio',
                'client_name': 'Fayvad Brand',
                'category_id': 1,
                'service_type': 'website',
                'short_description': 'Stunning creative portfolio showcasing brand design and marketing services',
                'description': '''Visually striking portfolio website for Fayvad Brand, highlighting creative services including logo design, brand identity development, and comprehensive marketing materials. The site demonstrates design capabilities through an immersive visual experience.

Features modern, image-heavy design with smooth animations, interactive portfolio galleries, and detailed case studies. Built to impress potential clients seeking professional branding and creative design services.

Includes comprehensive project showcases, detailed design process documentation, client testimonials, and an intuitive contact system for new business inquiries.''',
                'challenge': '''Fayvad Brand needed a portfolio website that would showcase their creative capabilities while maintaining professional credibility and effectively converting visitors into qualified leads for branding and design projects.''',
                'solution': '''Created a visually stunning portfolio website with emphasis on visual storytelling, interactive galleries, and smooth user experience. Implemented content management system for easy portfolio updates and integrated lead capture systems.''',
                'results': '''Launched a compelling brand portfolio that effectively showcases creative capabilities and has become a powerful tool for client acquisition. The site has improved brand perception and increased qualified inquiries for design services.''',
                'project_url': 'https://brand.fayvad.com',
                'demo_url': '',
                'completion_date': date(2024, 11, 15),
                'duration_months': 1,
                'project_cost': Decimal('120000.00'),
                'client_testimonial': 'Our new portfolio website beautifully showcases our creative work and has helped us attract higher-quality clients who appreciate good design.',
                'client_rating': 5,
                'status': 'completed',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Django', 'TailwindCSS', 'JavaScript', 'PostgreSQL', 'Cloudinary'],
                'meta_description': 'Creative portfolio for Fayvad Brand showcasing logo design, branding, and marketing services',
                'meta_keywords': 'Fayvad Brand, creative portfolio, logo design, brand identity, marketing materials'
            },
            
            # ERP & Business Solutions
            {
                'id': 3,
                'title': 'SME Inventory Management Solution',
                'slug': 'sme-inventory-management-solution',
                'client_name': 'Retail SME Client',
                'category_id': 2,
                'service_type': 'odoo',
                'short_description': 'Comprehensive inventory and sales management system using Odoo v17 CE',
                'description': '''Complete inventory and sales management solution for a growing retail SME, built on Odoo v17 Community Edition. The system streamlined stock management, sales processes, automated reordering, and improved financial reporting accuracy.

Customized Odoo modules to match specific business workflows including multi-location inventory tracking, automated reorder points, integrated POS functionality, and comprehensive reporting dashboards for better business insights and decision-making.

Implementation included data migration from legacy systems, staff training, and ongoing support to ensure smooth adoption and maximum benefit realization.''',
                'challenge': '''The client was struggling with manual inventory tracking, frequent stock-outs, inaccurate financial reporting, and inefficient sales processes that were limiting business growth and customer satisfaction.''',
                'solution': '''Implemented Odoo v17 CE with customized inventory modules, automated workflows, integrated POS system, and comprehensive reporting. Provided extensive training and change management support for smooth transition.''',
                'results': '''Achieved 95% improvement in inventory accuracy, 60% reduction in stock-outs, automated reorder processes, and real-time business insights. Client reported significant improvement in operational efficiency and customer satisfaction.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 10, 30),
                'duration_months': 3,
                'project_cost': Decimal('180000.00'),
                'client_testimonial': 'The Odoo system has transformed our inventory management. We now have real-time visibility into our stock levels and our ordering process is completely automated.',
                'client_rating': 5,
                'status': 'completed',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Odoo v17 CE', 'Python', 'PostgreSQL', 'Custom Modules', 'XML Reports'],
                'meta_description': 'SME inventory management solution using Odoo ERP for retail business automation',
                'meta_keywords': 'Odoo ERP, inventory management, retail solution, business automation, stock management'
            },
            {
                'id': 4,
                'title': 'SACCO Management Platform',
                'slug': 'sacco-management-platform',
                'client_name': 'Local SACCO',
                'category_id': 2,
                'service_type': 'custom',
                'short_description': 'Complete SACCO management solution with member portal and automated processes',
                'description': '''Comprehensive SACCO management platform combining Odoo backend with custom member portal. The solution handles member registration, share capital management, loan processing, savings tracking, dividend calculations, and financial reporting.

Built custom modules for SACCO-specific workflows including automated loan application processing, interest calculations, payment reminders, and member communication systems. The member portal enables self-service access to account information and transaction history.

Implementation included migration of existing member data, integration with M-Pesa payment systems, and comprehensive training for staff and members.''',
                'challenge': '''The SACCO needed to modernize manual processes for member management, loan processing, and financial operations while providing better member services and maintaining regulatory compliance.''',
                'solution': '''Developed integrated platform with Odoo backend for operations management and custom member portal for self-service. Implemented automated workflows for loan processing, payment handling, and member communication.''',
                'results': '''Reduced administrative workload by 70%, improved member satisfaction through self-service portal, automated loan processing from weeks to hours, and enhanced regulatory compliance through better record-keeping.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 9, 15),
                'duration_months': 4,
                'project_cost': Decimal('250000.00'),
                'client_testimonial': 'This system has revolutionized our operations. Our members love the self-service portal and our staff can focus on growth instead of paperwork.',
                'client_rating': 5,
                'status': 'completed',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Odoo v17 CE', 'Django Portal', 'PostgreSQL', 'M-Pesa Integration', 'Custom Modules'],
                'meta_description': 'SACCO management platform with member portal and automated loan processing',
                'meta_keywords': 'SACCO management, member portal, loan processing, cooperative finance, automated workflows'
            },
            
            # Non-Profit Solutions
            {
                'id': 5,
                'title': 'Makimei Children\'s Home Management System',
                'slug': 'makimei-childrens-home-management-system',
                'client_name': 'Makimei Children\'s Home',
                'category_id': 3,
                'service_type': 'custom',
                'short_description': 'Comprehensive child welfare management system for operational efficiency and compliance',
                'description': '''Specialized management system for Makimei Children\'s Home designed to streamline operations, improve child welfare tracking, and enhance organizational efficiency. The system manages comprehensive child records, educational progress monitoring, health tracking, donation management, and volunteer coordination.

Features include individual child profiles with detailed educational and health tracking, donation management with donor relationship tracking, volunteer scheduling and coordination, inventory management for supplies and equipment, and comprehensive reporting for compliance and funding applications.

The system is designed to help the children\'s home maintain better records, improve operational efficiency, demonstrate impact to donors and regulatory bodies, and ensure the best possible care for the children in their custody.''',
                'challenge': '''Makimei Children\'s Home needed a comprehensive system to track child welfare, manage donations efficiently, coordinate volunteers, maintain compliance records, and demonstrate impact to donors and authorities.''',
                'solution': '''Developing custom management system using Odoo framework with specialized modules for child welfare tracking, donation management, volunteer coordination, and comprehensive reporting for compliance and impact measurement.''',
                'results': '''Project in progress - Expected outcomes include 50% improvement in record-keeping accuracy, streamlined donor relations, better volunteer coordination, and enhanced ability to demonstrate impact for continued funding.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2025, 2, 28),
                'duration_months': 5,
                'project_cost': Decimal('200000.00'),
                'client_testimonial': 'We are excited about this system that will help us provide better care for our children while maintaining proper records for our donors and regulatory compliance.',
                'client_rating': None,
                'status': 'ongoing',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Odoo v17 CE', 'Custom Modules', 'PostgreSQL', 'Report Generation', 'Document Management'],
                'meta_description': 'Child welfare management system for Makimei Children\'s Home operational efficiency',
                'meta_keywords': 'children\'s home management, child welfare tracking, donation management, non-profit solutions'
            },
            {
                'id': 6,
                'title': 'Community Health Initiative Tracker',
                'slug': 'community-health-initiative-tracker',
                'client_name': 'Community Health Organization',
                'category_id': 3,
                'service_type': 'custom',
                'short_description': 'Health program tracking system for community outreach and patient management',
                'description': '''Community health tracking system designed to manage health outreach programs, patient records, and community health initiatives. The system helps track health interventions, measure program effectiveness, and coordinate community health workers.

Features include patient registration and follow-up tracking, health program management and scheduling, community health worker coordination and task assignment, medical supply inventory management, and outcome reporting for funders and health authorities.

Implementation improved program tracking capabilities, enabled evidence-based reporting for continued funding, and enhanced coordination between health workers and program managers.''',
                'challenge': '''The organization needed better tracking of community health programs, patient follow-ups, health worker coordination, and impact measurement for reporting to funders and health authorities.''',
                'solution': '''Built custom health tracking system with patient management, program coordination, health worker task management, and comprehensive reporting capabilities for impact measurement and compliance.''',
                'results': '''Improved program tracking efficiency by 80%, enabled better evidence-based reporting for continued funding, enhanced coordination between health workers, and provided clear impact metrics for program expansion.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 8, 20),
                'duration_months': 3,
                'project_cost': Decimal('150000.00'),
                'client_testimonial': 'This system has transformed how we track our community health programs. We can now easily demonstrate our impact to funders and coordinate our health workers more effectively.',
                'client_rating': 5,
                'status': 'completed',
                'featured': False,
                'show_in_portfolio': True,
                'technologies_used': ['Odoo v17 CE', 'Custom Health Modules', 'PostgreSQL', 'Mobile Integration'],
                'meta_description': 'Community health tracking system for program management and impact measurement',
                'meta_keywords': 'community health tracking, health program management, patient records, health initiatives'
            },
            
            # Domain & Infrastructure Projects
            {
                'id': 7,
                'title': 'Fayvad Digital Infrastructure Setup',
                'slug': 'fayvad-digital-infrastructure-setup',
                'client_name': 'Fayvad Digital',
                'category_id': 4,
                'service_type': 'hosting',
                'short_description': 'Complete digital infrastructure including domains, hosting, and email systems',
                'description': '''Comprehensive digital infrastructure establishment for Fayvad Digital including domain procurement and management, DNS configuration, hosting setup with load balancing, SSL certificate management, and professional email system configuration.

Managed complete domain portfolio including digital.fayvad.com, brand.fayvad.com, and related subdomains with proper DNS configuration, security protocols, and automated monitoring systems.

Implemented professional email systems using Zoho Mail with custom domain integration, security protocols (SPF, DKIM, DMARC), mobile device configuration for entire team, and comprehensive backup and security measures.''',
                'challenge': '''Fayvad Digital needed robust, scalable digital infrastructure that would support multiple brands, ensure high availability, maintain security standards, and provide professional communication systems.''',
                'solution': '''Designed and implemented comprehensive infrastructure with domain management, hosting configuration, email systems, security protocols, and monitoring systems to ensure reliable digital presence.''',
                'results': '''Established robust digital infrastructure supporting multiple brands with 99.9% uptime, professional email systems for team communication, automated security monitoring, and scalable hosting for future growth.''',
                'project_url': 'https://digital.fayvad.com',
                'demo_url': '',
                'completion_date': date(2024, 10, 1),
                'duration_months': 1,
                'project_cost': Decimal('75000.00'),
                'client_testimonial': 'Our digital infrastructure is now professional, reliable, and scalable. The email system works seamlessly and our websites load fast consistently.',
                'client_rating': 5,
                'status': 'completed',
                'featured': False,
                'show_in_portfolio': True,
                'technologies_used': ['DNS Management', 'Zoho Mail', 'SSL Certificates', 'Load Balancing', 'Security Monitoring'],
                'meta_description': 'Complete digital infrastructure setup for Fayvad Digital with domains, hosting, and email',
                'meta_keywords': 'digital infrastructure, domain management, hosting setup, email systems, DNS configuration'
            },
            {
                'id': 8,
                'title': 'Multi-Client Domain Management System',
                'slug': 'multi-client-domain-management-system',
                'client_name': 'Multiple SME Clients',
                'category_id': 4,
                'service_type': 'hosting',
                'short_description': 'Centralized domain and hosting management platform for multiple business clients',
                'description': '''Centralized management system for handling domain registration, renewal tracking, DNS management, and hosting services for multiple SME clients. The platform streamlines domain portfolio management and automates client communication for renewals and technical issues.

Features include automated renewal reminder systems, centralized DNS management interface, SSL certificate monitoring and renewal, client portal access for basic domain information, integrated billing system for seamless renewal processing, and comprehensive monitoring for uptime and performance.

Currently manages over 50 client domains with automated monitoring systems, eliminating domain expiration incidents and reducing manual oversight requirements.''',
                'challenge': '''Managing domains for multiple clients manually was time-consuming, prone to expiration oversights, and lacked centralized monitoring and client communication systems.''',
                'solution': '''Built centralized domain management platform with automated monitoring, renewal tracking, client portal access, and integrated billing system for efficient multi-client domain management.''',
                'results': '''Successfully managing 50+ client domains with automated monitoring, reduced manual oversight time by 90%, eliminated domain expiration incidents, and improved client satisfaction through proactive communication.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 11, 30),
                'duration_months': 2,
                'project_cost': Decimal('120000.00'),
                'client_testimonial': 'We never have to worry about domain renewals anymore. The system automatically reminds us and handles everything seamlessly.',
                'client_rating': 5,
                'status': 'completed',
                'featured': False,
                'show_in_portfolio': True,
                'technologies_used': ['Django', 'Domain APIs', 'PostgreSQL', 'Automated Monitoring', 'Client Portal'],
                'meta_description': 'Multi-client domain management system with automated renewal tracking and monitoring',
                'meta_keywords': 'domain management, automated renewals, multi-client platform, DNS management, hosting services'
            },
            
            # Training & Consulting Projects
            {
                'id': 9,
                'title': 'SME Digital Transformation Training Program',
                'slug': 'sme-digital-transformation-training-program',
                'client_name': 'Multiple SME Clients',
                'category_id': 5,
                'service_type': 'custom',
                'short_description': 'Comprehensive business process automation training for SME leaders and staff',
                'description': '''Comprehensive training program on business process automation and digital transformation specifically designed for SMEs and SACCOs in Kenya. The program covers digital strategy development, process identification and mapping, technology selection criteria, change management strategies, and implementation best practices.

Includes hands-on workshops with real business scenarios, case studies from successful digital transformations, practical exercises in process mapping and automation opportunity identification, and ongoing support for implementation planning.

The program has trained over 100 SME leaders and staff members across various industries, with measurable improvements in digital adoption and process efficiency.''',
                'challenge': '''SMEs lacked knowledge and practical guidance on how to identify automation opportunities, select appropriate technologies, and implement digital transformation initiatives successfully.''',
                'solution': '''Developed comprehensive training curriculum covering digital strategy, process automation, technology selection, and change management with hands-on workshops and real-world case studies.''',
                'results': '''Trained 100+ SME leaders with 85% implementing at least one automation solution within 6 months. Participants reported average productivity improvements of 30% in automated processes.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 12, 15),
                'duration_months': 6,
                'project_cost': Decimal('300000.00'),
                'client_testimonial': 'This training opened our eyes to automation opportunities we never saw before. We have already implemented three automated processes that save us hours each week.',
                'client_rating': 5,
                'status': 'completed',
                'featured': True,
                'show_in_portfolio': True,
                'technologies_used': ['Training Materials', 'Workshop Facilitation', 'Process Mapping', 'Case Studies'],
                'meta_description': 'SME digital transformation training program for business process automation',
                'meta_keywords': 'digital transformation training, business process automation, SME training, process improvement'
            },
            {
                'id': 10,
                'title': 'SACCO Digitization Strategic Consulting',
                'slug': 'sacco-digitization-strategic-consulting',
                'client_name': 'Regional SACCO Network',
                'category_id': 5,
                'service_type': 'custom',
                'short_description': 'Strategic consulting on digital transformation roadmap for SACCO network',
                'description': '''Strategic consulting engagement with regional SACCO network to develop comprehensive digital transformation roadmap. Conducted thorough assessment of current processes, identified technology gaps, and developed detailed digitization strategy with implementation phases and ROI projections.

Delivered comprehensive assessment reports covering current state analysis, technology gap identification, process optimization recommendations, phased implementation strategy with timelines and budgets, and detailed ROI projections for each transformation phase.

The consulting engagement resulted in adoption of standardized digital transformation approach across multiple SACCOs in the network.''',
                'challenge': '''Regional SACCO network needed strategic guidance on digital transformation approach, technology selection, implementation sequencing, and ROI measurement for their member SACCOs.''',
                'solution': '''Conducted comprehensive assessment of current state, developed strategic digital transformation roadmap with phased implementation approach, provided ROI projections and change management framework.''',
                'results': '''Delivered 3-year digital transformation plan adopted by 12 SACCOs in the network, with projected efficiency gains of 40% and improved member services across the network.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 7, 30),
                'duration_months': 3,
                'project_cost': Decimal('180000.00'),
                'client_testimonial': 'The strategic roadmap has given our network a clear path forward for digitization. We now have a practical plan that our member SACCOs can follow.',
                'client_rating': 5,
                'status': 'completed',
                'featured': False,
                'show_in_portfolio': True,
                'technologies_used': ['Strategic Planning', 'Process Analysis', 'ROI Modeling', 'Change Management'],
                'meta_description': 'SACCO network digital transformation strategic consulting and roadmap development',
                'meta_keywords': 'SACCO digitization, strategic consulting, digital transformation roadmap, process optimization'
            },
            {
                'id': 11,
                'title': 'Business Process Automation Masterclass Series',
                'slug': 'business-process-automation-masterclass-series',
                'client_name': 'Professional Development Initiative',
                'category_id': 5,
                'service_type': 'custom',
                'short_description': 'Intensive masterclass series on practical automation implementation',
                'description': '''Intensive masterclass series focused on practical business process automation implementation for business leaders and IT professionals. The program combines theoretical knowledge with hands-on implementation exercises and real-world automation projects.

Covers automation opportunity identification methodologies, tool evaluation and selection criteria, implementation planning and project management, change management for automation adoption, ROI measurement and success metrics, and ongoing optimization strategies.

Participants work on actual automation projects during the program, receiving guidance and feedback for practical implementation experience.''',
                'challenge': '''Business professionals needed practical, hands-on training in automation implementation beyond theoretical knowledge, with real-world application and measurable outcomes.''',
                'solution': '''Created intensive masterclass combining theory with practical implementation exercises, real automation projects, and ongoing mentorship for successful automation adoption.''',
                'results': '''Delivered program to 3 cohorts of professionals, with participants achieving average productivity improvements of 30% in automated processes and successful implementation of automation initiatives.''',
                'project_url': '',
                'demo_url': '',
                'completion_date': date(2024, 9, 30),
                'duration_months': 4,
                'project_cost': Decimal('200000.00'),
                'client_testimonial': 'The masterclass was incredibly practical. We didn\'t just learn about automation - we actually implemented working solutions during the program.',
                'client_rating': 5,
                'status': 'completed',
                'featured': False,
                'show_in_portfolio': True,
                'technologies_used': ['Training Curriculum', 'Automation Tools', 'Project Management', 'Assessment Framework'],
                'meta_description': 'Business process automation masterclass series with hands-on implementation training',
                'meta_keywords': 'automation masterclass, process automation training, hands-on training, automation implementation'
            }
        ]

        # Create portfolio projects
        created_count = 0
        updated_count = 0
        
        for project_data in portfolio_data:
            project, created = Portfolio.objects.get_or_create(
                id=project_data['id'],
                defaults=project_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created project: {project.title[:50]}...')
                )
            elif force:
                for key, value in project_data.items():
                    if key != 'id':
                        setattr(project, key, value)
                project.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Updated project: {project.title[:50]}...')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n📊 Portfolio summary: {created_count} created, {updated_count} updated')
        )