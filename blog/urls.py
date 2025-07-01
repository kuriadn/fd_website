# Create blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
    path('<slug:slug>/', views.blog_detail, name='detail'),
]

# Add to your main urls.py:
"""
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),  # Add this line
    path('contact/', include('contact.urls')),
]
"""