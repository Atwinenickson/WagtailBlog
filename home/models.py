from django.db import models

from wagtail.models import Page
from blog.models import BlogPage


class HomePage(Page):
    
    def get_context(self, request):
        context = super().get_context(request)
        featured_articles = BlogPage.objects.live().filter(featured=True)
        context['featured_articles'] = featured_articles
        return context
