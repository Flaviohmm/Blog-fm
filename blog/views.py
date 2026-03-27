from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Post, Category


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
    

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.select_related('category').prefetch_related('tags').order_by('-published_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    