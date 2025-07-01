# Create portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='list'),
    path('<slug:slug>/', views.portfolio_detail, name='detail'),
]

# Add to your main urls.py:
"""
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),  # Add this line
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
]
"""