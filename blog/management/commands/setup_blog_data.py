# blog/management/commands/setup_blog_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import BlogCategory, BlogPost
from datetime import datetime 
import pytz
import json


class Command(BaseCommand):
    help = 'Creates blog authors and loads starter blog data for Fayvad Digital'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite existing data',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Setting up Fayvad Digital blog data...\n')
        )

        # Create authors
        self.create_authors(force=options['force'])
        
        # Load blog data
        self.load_blog_data(force=options['force'])
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Blog setup completed successfully!')
        )
        self.stdout.write(
            self.style.WARNING('📝 Remember to update author passwords in Django admin')
        )

    def create_authors(self, force=False):
        """Create the two blog authors"""
        
        authors_data = [
            {
                'id': 1,
                'username': 'david.kuria',
                'email': 'david.kuria@fayvad.com',
                'first_name': 'David',
                'last_name': 'Kuria',
                'is_staff': True,
                'is_active': True,
            },
            {
                'id': 2,
                'username': 'moses.gashusha',
                'email': 'm.gashusha@digital.fayvad.com', 
                'first_name': 'Moses',
                'last_name': 'Gashusha',
                'is_staff': True,
                'is_active': True,
            }
        ]

        for author_data in authors_data:
            user, created = User.objects.get_or_create(
                id=author_data['id'],
                defaults=author_data
            )
            
            if created:
                # Set a default password (users should change this)
                user.set_password('fayvad2024!')
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created author: {user.get_full_name()} ({user.email})')
                )
            elif force:
                # Update existing user
                for key, value in author_data.items():
                    if key != 'id':
                        setattr(user, key, value)
                user.save()
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Updated existing author: {user.get_full_name()}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Author already exists: {user.get_full_name()}')
                )

    def load_blog_data(self, force=False):
        """Load blog categories and posts"""
        
        # Blog Categories
        categories_data = [
            {
                'id': 1,
                'name': 'Digital Transformation',
                'slug': 'digital-transformation',
                'description': 'Insights and strategies for successful business digitization',
                'color': '#3B82F6',
                'is_active': True
            },
            {
                'id': 2,
                'name': 'Business Technology',
                'slug': 'business-technology',
                'description': 'Technology solutions for modern businesses',
                'color': '#059669',
                'is_active': True
            },
            {
                'id': 3,
                'name': 'ERP & Automation',
                'slug': 'erp-automation',
                'description': 'Enterprise Resource Planning and business automation insights',
                'color': '#7C3AED',
                'is_active': True
            }
        ]

        # Create categories
        for cat_data in categories_data:
            category, created = BlogCategory.objects.get_or_create(
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

        # Blog Posts
        posts_data = [
            {
                'id': 1,
                'title': 'The Digital Transformation Journey: A Guide for Kenyan SMEs',
                'slug': 'digital-transformation-journey-kenyan-smes',
                'excerpt': 'Digital transformation isn\'t just a buzzword—it\'s a necessity for SMEs looking to thrive in today\'s competitive landscape. Learn how to navigate this journey successfully.',
                'content': self.get_post_content_1(),
                'meta_title': 'Digital Transformation Guide for Kenyan SMEs | Fayvad Digital',
                'meta_description': 'Complete guide to digital transformation for Kenyan SMEs. Learn steps, overcome challenges, and discover success stories from local businesses.',
                'category_id': 1,
                'tags': 'digital transformation, SMEs, Kenya, business automation, technology adoption',
                'status': 'published',
                'is_featured': True,
                'published_at': datetime(2024, 12, 15, 9, 0, 0, tzinfo=pytz.UTC),
                'author_id': 1,
                'view_count': 247
            },
            {
                'id': 2,
                'title': 'Technology Onboarding: Setting Your Team Up for Success',
                'slug': 'technology-onboarding-team-success',
                'excerpt': 'Implementing new technology is only half the battle. Learn proven strategies for successfully onboarding your team and ensuring adoption of new digital tools.',
                'content': self.get_post_content_2(),
                'meta_title': 'Technology Onboarding Best Practices | Team Training Guide',
                'meta_description': 'Learn proven strategies for successful technology onboarding. Discover how to train your team effectively and ensure adoption of new digital tools.',
                'category_id': 2,
                'tags': 'technology onboarding, team training, change management, digital adoption, user training',
                'status': 'published',
                'is_featured': True,
                'published_at': datetime(2024, 12, 10, 14, 30, 0, tzinfo=pytz.UTC),
                'author_id': 2,
                'view_count': 189
            },
            {
                'id': 3,
                'title': 'Why Your Growing Business Needs an ERP System: A Comprehensive Guide',
                'slug': 'why-business-needs-erp-system-guide',
                'excerpt': 'As your business grows, managing operations becomes increasingly complex. Discover how an ERP system can streamline your processes and support sustainable growth.',
                'content': self.get_post_content_3(),
                'meta_title': 'Why Your Growing Business Needs an ERP System | Complete Guide',
                'meta_description': 'Discover why ERP systems are essential for growing businesses. Learn benefits, implementation best practices, and how to choose the right ERP solution.',
                'category_id': 3,
                'tags': 'ERP system, business growth, Odoo ERP, enterprise resource planning, business automation',
                'status': 'published',
                'is_featured': True,
                'published_at': datetime(2024, 12, 5, 11, 15, 0, tzinfo=pytz.UTC),
                'author_id': 1,
                'view_count': 312
            },
            {
                'id': 4,
                'title': 'The Power of Business Process Automation: Transform Your Operations',
                'slug': 'business-process-automation-transform-operations',
                'excerpt': 'Manual processes are holding your business back. Learn how automation can eliminate repetitive tasks, reduce errors, and free your team to focus on growth.',
                'content': self.get_post_content_4(),
                'meta_title': 'Business Process Automation Benefits | Transform Operations Guide',
                'meta_description': 'Discover how business process automation can eliminate manual tasks, reduce errors, and boost productivity. Learn implementation strategies and ROI calculations.',
                'category_id': 3,
                'tags': 'business process automation, workflow automation, productivity, efficiency, business optimization',
                'status': 'published',
                'is_featured': False,
                'published_at': datetime(2024, 11, 28, 13, 45, 0, tzinfo=pytz.UTC),
                'author_id': 2,
                'view_count': 156
            },
            {
                'id': 5,
                'title': 'Boosting Revenue Through Strategic Technology Investments',
                'slug': 'boosting-revenue-strategic-technology-investments',
                'excerpt': 'Technology isn\'t just a cost center—it\'s a revenue driver. Learn how smart technology investments can directly increase your business revenue and profitability.',
                'content': self.get_post_content_5(),
                'meta_title': 'How Technology Investments Drive Revenue Growth | Business Guide',
                'meta_description': 'Learn how strategic technology investments directly increase business revenue. Discover ROI strategies, implementation phases, and real success stories.',
                'category_id': 2,
                'tags': 'revenue growth, technology ROI, business technology, digital transformation, profit optimization',
                'status': 'published',
                'is_featured': False,
                'published_at': datetime(2024, 11, 20, 10, 30, 0, tzinfo=pytz.UTC),
                'author_id': 1,
                'view_count': 198
            },
            {
                'id': 6,
                'title': 'Digital Innovation in African SACCOs: Leading the Financial Inclusion Revolution',
                'slug': 'digital-innovation-african-saccos-financial-inclusion',
                'excerpt': 'SACCOs across Africa are embracing digital transformation to better serve their members and expand financial inclusion. Discover the latest innovations and success strategies.',
                'content': self.get_post_content_6(),
                'meta_title': 'Digital Innovation in African SACCOs | Financial Inclusion Revolution',
                'meta_description': 'Explore how SACCOs across Africa are using digital innovation to transform financial inclusion. Success stories, strategies, and implementation guides.',
                'category_id': 1,
                'tags': 'SACCOs, financial inclusion, digital banking, Africa, cooperative finance, fintech',
                'status': 'published',
                'is_featured': False,
                'published_at': datetime(2024, 11, 15, 8, 20, 0, tzinfo=pytz.UTC),
                'author_id': 1,
                'view_count': 134
            }
        ]

        # Create blog posts
        created_count = 0
        updated_count = 0
        
        for post_data in posts_data:
            post, created = BlogPost.objects.get_or_create(
                id=post_data['id'],
                defaults=post_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created post: {post.title[:50]}...')
                )
            elif force:
                for key, value in post_data.items():
                    if key != 'id':
                        setattr(post, key, value)
                post.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Updated post: {post.title[:50]}...')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n📊 Blog posts summary: {created_count} created, {updated_count} updated')
        )

    def get_post_content_1(self):
        return """Digital transformation has become more than just a trend; it's now essential for Small and Medium Enterprises (SMEs) in Kenya who want to remain competitive and grow sustainably.

## Understanding Digital Transformation

Digital transformation involves integrating digital technology into all areas of your business, fundamentally changing how you operate and deliver value to customers. For Kenyan SMEs, this means moving from traditional manual processes to automated, technology-driven solutions.

## Why SMEs Need Digital Transformation

**1. Improved Efficiency**
Automating routine tasks frees up your team to focus on strategic activities that drive growth. Instead of spending hours on manual data entry, your staff can concentrate on customer service and business development.

**2. Better Customer Experience**
Digital tools enable you to serve customers faster and more accurately. Online ordering systems, customer portals, and mobile apps make it easier for customers to do business with you.

**3. Data-Driven Decisions**
Digital systems generate valuable data about your operations, customers, and market trends. This information helps you make informed decisions rather than relying on guesswork.

**4. Cost Reduction**
While there's an initial investment, digital transformation typically reduces long-term operational costs through automation and improved efficiency.

## Steps to Start Your Digital Journey

**Step 1: Assess Your Current State**
Evaluate your existing processes and identify areas where technology could make the biggest impact. Common starting points include customer management, inventory tracking, financial management, and communication systems.

**Step 2: Set Clear Goals**
Define what you want to achieve through digitization. Whether it's reducing processing time by 50% or improving customer satisfaction scores, having clear objectives guides your technology choices.

**Step 3: Start Small**
Begin with one or two key processes rather than trying to digitize everything at once. This approach allows you to learn and adjust before scaling up.

**Step 4: Choose the Right Partner**
Working with experienced technology partners like Fayvad Digital ensures you get solutions that fit your specific needs and budget.

At Fayvad Digital, we've helped over 500 SMEs begin their digital transformation journey. We understand the unique challenges facing Kenyan businesses and provide solutions that deliver real results.

**Ready to start your digital transformation?** Contact us for a free consultation to discuss how we can help your business thrive in the digital age."""

    def get_post_content_2(self):
        return """The success of any technology implementation depends heavily on how well your team adapts to and adopts the new tools. Poor onboarding can turn even the best technology solutions into expensive paperweights.

## The Critical First 30 Days

The first month after implementing new technology is crucial. This period determines whether your investment will pay off or become a source of frustration for your team.

## Pre-Implementation Planning

**Identify Champions**
Select team members who are enthusiastic about technology and can become internal advocates. These champions will help train others and provide peer support during the transition.

**Assess Current Skills**
Understand your team's existing technology skills. This assessment helps you design appropriate training programs and identify who might need extra support.

**Communicate the 'Why'**
Before introducing new technology, explain why it's necessary and how it will benefit both the business and individual employees. People resist change less when they understand its purpose.

## Effective Training Strategies

**1. Hands-On Learning**
Use real business scenarios during training rather than generic examples. If you're implementing an inventory system, train using your actual products and processes.

**2. Progressive Disclosure**
Don't overwhelm users with every feature on day one. Start with basic functions they'll use daily, then gradually introduce advanced features.

**3. Multiple Learning Formats**
- Live training sessions for interactive learning
- Video tutorials for self-paced learning
- Quick reference guides for daily use
- One-on-one support for struggling users

At Fayvad Digital, we don't just implement technology—we ensure your team is fully prepared to leverage it effectively. Our comprehensive training and support programs have helped hundreds of teams successfully adopt new digital tools.

**Need help with technology onboarding?** Our experts can design a customized training program that ensures your team embraces and effectively uses new technology from day one."""

    def get_post_content_3(self):
        return """When businesses start small, entrepreneurs can manage everything manually—tracking inventory on spreadsheets, handling customer relationships through personal contacts, and managing finances with basic accounting software. However, as the business grows, this approach becomes unsustainable.

## What is an ERP System?

An Enterprise Resource Planning (ERP) system is integrated software that manages and automates core business processes including financial management, customer relationship management, inventory management, human resources, project management, and reporting.

## Signs Your Business Needs an ERP System

**1. Information Silos**
When different departments use separate systems that don't communicate with each other, you lose valuable insights and efficiency.

**2. Manual Processes Consuming Too Much Time**
If your team spends significant time on data entry, reconciling information across systems, or generating reports manually, an ERP system can automate these tasks.

**3. Difficulty Getting Accurate Reports**
When business decisions are delayed because you can't quickly access accurate, up-to-date information, it's time to consider ERP integration.

## Key Benefits of ERP Implementation

### Improved Efficiency
ERP systems automate routine tasks like order processing, invoice generation, and inventory updates. This automation reduces manual work and minimizes errors.

### Better Decision Making
Real-time data and comprehensive reporting tools help you understand business performance, identify trends, and spot opportunities for improvement.

### Enhanced Customer Service
With all customer information in one system, your team can provide more personalized and efficient service.

## The Odoo Advantage

At Fayvad Digital, we specialize in Odoo ERP implementations because it offers comprehensive functionality at affordable prices, modular approach allowing gradual expansion, user-friendly interface requiring minimal training, and strong integration capabilities.

**Ready to explore ERP options for your business?** Contact us for a free consultation to discuss how an ERP system can support your growth objectives and improve your operational efficiency."""

    def get_post_content_4(self):
        return """Business process automation (BPA) has evolved from a luxury for large corporations to a necessity for businesses of all sizes. In today's competitive landscape, manual processes are not just inefficient—they're a barrier to growth and profitability.

## Understanding Business Process Automation

Business process automation involves using technology to perform recurring tasks or processes where manual effort can be replaced. This doesn't mean replacing people; it means freeing them from repetitive work so they can focus on strategic, creative, and relationship-building activities.

## The Hidden Costs of Manual Processes

**Time Wastage**
Studies show that employees spend up to 40% of their time on repetitive, manual tasks that could be automated. For a team of 10 employees, this represents 4 full-time positions worth of productivity lost to inefficiency.

**Human Error**
Manual data entry has an average error rate of 1-5%. While this might seem small, consider the cumulative impact on inventory counts, billing accuracy, and data consistency.

## Key Areas for Automation in SMEs

### Customer Relationship Management
- Automatic lead capture and qualification
- Automated follow-up sequences
- Customer segmentation and service

### Financial Operations
- Invoice generation and payment processing
- Expense approval workflows
- Financial reporting automation

### Inventory Management
- Automatic reorder points
- Supplier notifications
- Cycle counting schedules

## Benefits of Process Automation

**Increased Productivity**
Automation can improve productivity by 20-30% in the first year by eliminating manual tasks and reducing processing time.

**Reduced Errors**
Automated processes have error rates near zero, compared to 1-5% for manual processes.

**Scalability**
Automated processes can handle increased volume without proportional increases in staff, enabling sustainable growth.

At Fayvad Digital, we specialize in helping SMEs and SACCOs identify and implement practical automation solutions. Our experience with hundreds of businesses has shown us which automations deliver the fastest returns.

**Ready to transform your operations through automation?** Contact us for a free process assessment and discover how automation can eliminate bottlenecks, reduce costs, and accelerate your business growth."""

    def get_post_content_5(self):
        return """Many business owners view technology as a necessary expense, but savvy entrepreneurs understand that the right technology investments can directly drive revenue growth. In fact, businesses that strategically leverage technology typically see 20-30% higher revenue growth than those that don't.

## Technology as a Revenue Driver

Unlike traditional business expenses, technology investments can multiply your revenue-generating capacity. A well-implemented CRM system doesn't just organize customer data—it helps you sell more to existing customers and acquire new ones more efficiently.

## Direct Revenue Enhancement Strategies

### Customer Relationship Optimization
CRM systems provide deep insights into customer behavior, preferences, and buying patterns. This data enables targeted marketing campaigns, personalized recommendations, and optimal sales timing.

**Revenue Impact**: Businesses using CRM systems see an average revenue increase of 15-25% within the first year.

### Sales Process Optimization
Automated sales processes reduce the time from lead to close through instant quote generation, automated proposals, digital contracts, and streamlined approvals.

**Revenue Impact**: Reducing sales cycle time by 20% can increase annual revenue by 15-30%.

### E-commerce and Digital Sales Channels
Digital platforms open new revenue opportunities with 24/7 availability, geographic expansion, reduced costs, and scalable operations.

**Revenue Impact**: SMEs adding e-commerce typically see 20-40% revenue growth in the first year.

## Technology Investment Categories with Highest ROI

### CRM Platforms
- Average ROI: 400-800% over 3 years
- Revenue increase: 15-25% annually
- Customer retention improvement: 10-15%

### E-commerce Platforms
- Average ROI: 300-600% over 2 years
- New revenue potential: 20-40% of total revenue

### Marketing Automation
- Average ROI: 400-700% over 2 years
- Lead generation increase: 50-100%
- Conversion rate improvement: 20-30%

At Fayvad Digital, we've helped hundreds of SMEs and SACCOs implement technology solutions that directly impact their bottom line. Our focus isn't just on making your operations more efficient—it's on making your business more profitable.

**Ready to turn technology into a revenue driver?** Contact us for a free revenue impact assessment."""

    def get_post_content_6(self):
        return """Savings and Credit Cooperative Organizations (SACCOs) have long been pillars of financial inclusion in Africa, serving communities that traditional banks often overlook. Today, these member-owned institutions are at the forefront of a digital revolution that's transforming how financial services are delivered across the continent.

## The Digital Imperative for SACCOs

African SACCOs serve over 50 million members across the continent, managing assets worth billions of dollars. However, many still rely on manual processes that limit their ability to serve members efficiently and compete with digital-first financial services.

## Key Digital Innovation Areas

### Core Banking Systems
Modern SACCO management platforms provide real-time transaction processing, automated loan calculations, member account management, and integration capabilities.

**Benefits:**
- Reduced transaction time from hours to minutes
- Improved accuracy and reduced errors
- Better member experience
- Enhanced regulatory compliance

### Mobile Banking and Apps
Member-facing applications enable account inquiries, transaction history, loan applications, mobile transfers, and bill payments.

**Impact on Member Engagement:**
- 60-80% increase in transaction frequency
- 40-50% reduction in branch visits
- Improved member satisfaction
- Enhanced financial literacy

### Digital Lending Platforms
Automated loan processing provides online applications, automated credit scoring, digital documents, real-time approvals, and automated disbursement.

**Results:**
- Loan processing reduced from weeks to hours
- 30-50% increase in loan portfolio
- Improved risk assessment
- Better monitoring and collection

## Success Stories Across Africa

### Kenya - Stima SACCO
- 70% reduction in transaction processing time
- 45% increase in loan portfolio
- 60% improvement in member satisfaction
- 25% growth in membership

### Uganda - Kampala City SACCO
- 80% of transactions through mobile platform
- 35% increase in deposits
- 50% reduction in operational costs
- Service expansion without new branches

## Implementation Strategies

### Phase 1: Foundation (Months 1-6)
Core system implementation, basic member portal, digital account opening, electronic document management.

### Phase 2: Member Engagement (Months 7-12)
Mobile banking app, USSD services, online loan applications, digital payment integration.

### Phase 3: Innovation (Year 2+)
AI-powered credit scoring, predictive analytics, blockchain transparency, IoT for agricultural lending.

At Fayvad Digital, we understand the unique challenges and opportunities facing African SACCOs. Our experience working with cooperative financial institutions across the region has taught us that successful digitization requires understanding of cooperative principles, member needs, and local market dynamics.

**Ready to lead your SACCO's digital transformation?** Contact us to learn how our SACCO-specific solutions can help you serve your members better while building a sustainable digital future."""