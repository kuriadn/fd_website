from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class PagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact', 'services']

    def location(self, item):
        return reverse(item)