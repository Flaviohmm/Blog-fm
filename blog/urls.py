from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("blog/", views.BlogListView.as_view(), name="blog_list"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("sobre/", views.AboutView.as_view(), name="about"),
]