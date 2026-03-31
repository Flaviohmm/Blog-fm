# blog/templatetags/clean_html.py
from django import template
import re

register = template.Library()

@register.filter
def clean_html(html_content):
    if not html_content:
        return ""

    # Remove &nbsp; excessivos
    html = re.sub(r'&nbsp;', ' ', html_content)
    
    # Remove estilos inline margin-left
    html = re.sub(r'style="margin-left:0px;"', '', html)
    html = re.sub(r'style="margin-left:\s*0px;"', '', html)
    
    # Remove data-list-item-id
    html = re.sub(r'data-list-item-id="[^"]*"', '', html)
    
    # Remove espaços vazios excessivos
    html = re.sub(r'\s+', ' ', html)
    
    # Corrige listas quebradas
    html = re.sub(r'<p>\s*</p>', '', html)
    
    return html.strip()