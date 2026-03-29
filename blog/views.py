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

        context['featured_posts'] = [
            {
                "title": "Por que migrei 100% para Linux em 2026",
                "category": "Linux",
                "date": "20 Mar 2026",
                "read_time": "5 min",
                "slug": "#"
            },
            {
                "title": "Bitcoin como reserva de valor: uma análise racional",
                "category": "Economia",
                "date": "15 Mar 2026",
                "read_time": "8 min",
                "slug": "#"
            },
            {
                "title": "Self-hosting: liberdade digital na prática",
                "category": "Tecnologia",
                "date": "10 Mar 2026",
                "read_time": "6 min",
                "slug": "#"
            },
        ]

        return context
    

class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.select_related('category').prefetch_related('tags').order_by('-published_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'  

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs) 

        context['projects'] = [
            {
                'title': 'dotfiles',
                'description': 'Minha configuração pessoal para Arch Linux, Hyprland, Neovim e terminal. Totalmente automatizada.',
                'tags': ['Linux', 'Bash', 'Neovim', 'Dotfiles'],
                'category': 'Open Source',
                'github': 'https://github.com/Flaviohm_2/dotfiles',
                'demo': None
            },
            {
                'title': 'budget-tracker',
                'description': 'App web para controle financeiro pessoal com categorias, gráficos e exportação CSV.',
                'tags': ['Django', 'Tailwind', 'Python'],
                'category': 'Web',
                'github': 'https://github.com/Flaviohm_2/budget-tracker',
                'demo': '#'
            },
            {
                'title': 'docker-homelab',
                'description': 'Stack completa de self-hosting com Docker Compose: Nextcloud, Vaultwarden, Gitea e mais.',
                'tags': ['Docker', 'Linux', 'Nginx'],
                'category': 'DevOps',
                'github': 'https://github.com/Flaviohm_2/homelab',
                'demo': None
            },
            # Adicione mais projetos conforme necessário
        ]

        context['categories'] = ["Todos", "Open Source", "Web", "DevOps", "CLI"]

        return context
    

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['values'] = [
            {
                "icon": "Terminal",
                "label": "Open Source",
                "text": "Acredito que software deve ser livre e acessível. Contribuo e uso Linux diariamente."
            },
            {
                "icon": "BookOpen",
                "label": "Pensamento Crítico",
                "text": "Questionar é fundamental. Busco entender os 'porquês' antes de aceitar qualquer narrativa."
            },
            {
                "icon": "Shield",
                "label": "Privacidade Digital",
                "text": "Seus dados são seus. Defendo e pratico hábitos de privacidade digital no dia a dia."
            },
            {
                "icon": "Heart",
                "label": "Liberdade Individual",
                "text": "Menos estado, mais liberdade. Acredito no poder da ação individual e do livre mercado."
            },
        ]

        context['tools'] = [
            "Arch Linux", "Neovim", "Docker", "Rust", "Python", 
            "TypeScript", "React", "Next.js", "Tailwind CSS", 
            "Git", "Nginx", "PostgreSQL"
        ]

        return context