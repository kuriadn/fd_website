# Fayvad Digital Website

Professional Django website for Fayvad Digital - empowering SMEs & SACCOs with smart digital solutions.

## 🚀 Features

- **Modern Django Architecture** - Clean, scalable project structure
- **Responsive Design** - Mobile-first design with Tailwind CSS
- **Service Management** - Dynamic service categories and pricing
- **Contact System** - Contact forms with email notifications
- **Blog System** - Content marketing capabilities
- **SEO Optimized** - Meta tags, sitemaps, and structured data
- **Admin Ready** - Django admin for content management

## 🛠️ Tech Stack

- **Backend**: Django 5.0+
- **Database**: PostgreSQL (SQLite for development)
- **Frontend**: Tailwind CSS + Alpine.js
- **Email**: Django email backend
- **Deployment**: Docker + Nginx

## 📋 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fayvad-digital-website
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to see the website.

## 🐳 Docker Setup

```bash
# Development
docker-compose up --build

# Production
docker-compose -f docker-compose.prod.yml up --build
```

## 📁 Project Structure

```
fayvad_digital/
├── fayvad_digital/          # Main project settings
├── apps/
│   ├── core/               # Core models and utilities
│   ├── pages/              # Static pages (home, about)
│   ├── services/           # Service management
│   ├── contact/            # Contact forms
│   └── blog/              # Blog system
├── static/                 # Static files
├── media/                  # User uploads
├── templates/              # HTML templates
├── requirements.txt        # Python dependencies
└── manage.py              # Django management
```

## 🎨 Customization

### Adding New Services
1. Log into Django admin (`/admin/`)
2. Go to Services section
3. Add new service categories and services

### Updating Content
- **Homepage**: Edit templates/pages/home.html
- **Styling**: Modify static/css/custom.css
- **Contact Info**: Update in Django admin or templates

## 🚀 Deployment

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost/dbname
EMAIL_HOST=smtp.example.com
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Production Checklist
- [ ] Set DEBUG=False
- [ ] Configure PostgreSQL
- [ ] Set up email backend
- [ ] Configure static file serving
- [ ] Set up SSL certificate
- [ ] Configure domain and DNS

## 📞 Contact

**Fayvad Digital**
- Website: [digital.fayvad.com](http://digital.fayvad.com)
- Email: services@digital.fayvad.com
- Phone: +254-769-069-640

## 📄 License

This project is proprietary to Fayvad Digital.