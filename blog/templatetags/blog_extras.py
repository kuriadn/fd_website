from django import template
import markdown

register = template.Library()

@register.filter
def markdown_to_html(value):
    """Convert markdown text to HTML"""
    if not value:
        return ""
    return markdown.markdown(
        value, 
        extensions=['extra', 'codehilite', 'toc']
    )