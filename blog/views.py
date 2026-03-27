from typing import Any

from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['topics'] = [
            {
                "icon": "terminal", 
                "label": "Linux & Open Source", 
                "description": "Explorando o poder do software livre e sistemas Unix-like."
            },
            {
                "icon": "cpu", 
                "label": "Tecnologia & Dev", 
                "description": "IA, desenvolvimento, DevOps e o futuro da computação."
            },
            {
                "icon": "trending-up", 
                "label": "Economia", 
                "description": "Análise macro, investimentos, Bitcoin e finanças pessoais."
            },
            {
                "icon": "shield", 
                "label": "Privacidade", 
                "description": "Ferramentas e práticas para proteger sua liberdade digital."
            },
            {
                "icon": "globe", 
                "label": "Política & Liberdade", 
                "description": "Pensamento liberal, liberdade individual e crítica ao estatismo."
            },
        ]

        context['featured_posts'] = Post.objects.filter(published_at__isnull=False).order_by('-published_at')[:3]

        return context