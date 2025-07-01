# Sample data to add via Django admin - services/fixtures/sample_services.py
# You can use this as reference when adding services through admin

SAMPLE_CATEGORIES = [
    {
        'name': 'Web Solutions',
        'slug': 'web-solutions',
        'description': 'Professional websites and e-commerce solutions'
    },
    {
        'name': 'Business Systems',
        'slug': 'business-systems', 
        'description': 'ERP and CRM solutions for business automation'
    },
    {
        'name': 'Hosting & Domains',
        'slug': 'hosting-domains',
        'description': 'Reliable hosting and domain services'
    },
    {
        'name': 'Training & Support',
        'slug': 'training-support',
        'description': 'Digital training and ongoing support services'
    }
]

SAMPLE_SERVICES = [
    {
        'name': 'Starter Website',
        'slug': 'starter-website',
        'category': 'web-solutions',
        'short_description': '5-page responsive website with basic SEO and 1-year hosting',
        'description': 'Perfect for small businesses getting started online. Includes professional design, mobile-responsive layout, contact forms, and basic SEO optimization.',
        'features': [
            '5 professional pages',
            'Mobile-responsive design', 
            'Contact form integration',
            'Basic SEO optimization',
            '1-year hosting included',
            'SSL certificate',
            'Google Analytics setup'
        ],
        'price': 20000,
        'setup_fee': 0,
        'billing_cycle': 'one_time',
        'is_featured': True,
        'benefits': 'Establish your online presence quickly and affordably. Perfect for service businesses, consultants, and small retailers.',
        'requirements': 'Business information, logo, and content. We can help with content creation if needed.',
        'process': '1. Discovery call\n2. Design mockup\n3. Development\n4. Review and revisions\n5. Launch and training'
    },
    {
        'name': 'Business Website',
        'slug': 'business-website',
        'category': 'web-solutions',
        'short_description': '10 pages with contact forms, blog, and advanced SEO features',
        'description': 'Comprehensive business website with all the features you need to compete online. Includes blog functionality, advanced SEO, and professional design.',
        'features': [
            '10 custom pages',
            'Blog functionality',
            'Advanced SEO optimization',
            'Contact forms',
            'Social media integration',
            'Google Analytics & Search Console',
            'SSL certificate',
            '1-year hosting'
        ],
        'price': 35000,
        'setup_fee': 0,
        'billing_cycle': 'one_time',
        'is_featured': True,
        'benefits': 'Complete online presence with content marketing capabilities. Ideal for growing businesses that want to attract customers online.',
        'requirements': 'Business information, branding materials, content outline. We provide content guidance.',
        'process': '1. Strategy session\n2. Sitemap and wireframes\n3. Design and development\n4. Content integration\n5. SEO setup\n6. Launch and training'
    },
    {
        'name': 'E-commerce Website',
        'slug': 'ecommerce-website',
        'category': 'web-solutions',
        'short_description': 'Full online store with payment integration and 20 products uploaded',
        'description': 'Complete e-commerce solution with M-PESA integration, inventory management, and order processing. Perfect for retailers ready to sell online.',
        'features': [
            'Full online store',
            'M-PESA payment integration',
            'Inventory management',
            'Order processing system',
            '20 products uploaded',
            'Customer accounts',
            'Mobile-responsive design',
            'SSL certificate',
            'Basic analytics'
        ],
        'price': 60000,
        'setup_fee': 0,
        'billing_cycle': 'one_time',
        'is_featured': True,
        'benefits': 'Start selling online immediately with secure payment processing. Expand your market reach beyond physical location.',
        'requirements': 'Product information, images, business registration, payment processor setup assistance.',
        'process': '1. Requirements gathering\n2. Payment setup\n3. Store development\n4. Product upload\n5. Testing\n6. Launch and training'
    },
    {
        'name': 'Odoo ERP Starter',
        'slug': 'odoo-erp-starter',
        'category': 'business-systems',
        'short_description': 'CRM, Sales, and Invoicing modules for 5 users with hosting',
        'description': 'Get started with Odoo ERP with essential business modules. Includes setup, customization, training, and cloud hosting.',
        'features': [
            'CRM module setup',
            'Sales management',
            'Invoicing system',
            '5 user accounts',
            'Cloud hosting included',
            'Data migration assistance',
            'User training (2 sessions)',
            'Email integration',
            'Mobile app access'
        ],
        'price': 35000,
        'setup_fee': 0,
        'billing_cycle': 'one_time',
        'monthly_fee': 3500,
        'is_featured': False,
        'benefits': 'Streamline your sales process and customer management. Perfect for service businesses and small manufacturers.',
        'requirements': 'Existing customer data (if any), business process information, user list.',
        'process': '1. Business analysis\n2. System setup\n3. Data migration\n4. Customization\n5. User training\n6. Go-live support'
    },
    {
        'name': 'Zoho Mail Setup',
        'slug': 'zoho-mail-setup',
        'category': 'business-systems',
        'short_description': 'Professional email setup with domain integration and training',
        'description': 'Professional email solution with your domain. Includes setup, DNS configuration, and user training.',
        'features': [
            'Professional email accounts',
            'Domain integration',
            'DNS configuration',
            'Mobile device setup',
            'Email signatures',
            'User training',
            'Security setup',
            'Calendar integration'
        ],
        'price': 15000,
        'setup_fee': 0,
        'billing_cycle': 'one_time',
        'is_featured': False,
        'benefits': 'Professional email addresses boost credibility and improve communication with customers.',
        'requirements': 'Domain ownership or new domain purchase, list of required email addresses.',
        'process': '1. Domain verification\n2. Email setup\n3. DNS configuration\n4. Device configuration\n5. User training'
    },
    {
        'name': 'Domain Registration',
        'slug': 'domain-registration',
        'category': 'hosting-domains',
        'short_description': '.com or .org domain registration with DNS management',
        'description': 'Secure your business domain name with professional DNS management and support.',
        'features': [
            '.com or .org registration',
            'DNS management',
            'Email forwarding',
            'Domain privacy protection',
            'Free SSL certificate',
            '24/7 support',
            'Easy renewal management'
        ],
        'price': 3500,
        'setup_fee': 0,
        'billing_cycle': 'yearly',
        'is_featured': False,
        'benefits': 'Establish your online identity with a professional domain name.',
        'requirements': 'Business information for domain registration.',
        'process': '1. Domain search\n2. Registration\n3. DNS setup\n4. Email configuration'
    }
]