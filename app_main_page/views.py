import random
from django.views.generic import TemplateView
from app_publications.models import Posts


class AppMainPageView(TemplateView):
    """Главная страница"""
    template_name = 'app_main_page/main.html'
    extra_context = {
        'title': 'place_in_space: Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        count_post = len(Posts.objects.filter(is_published=True))
        if count_post > 0:
            blog_6_post = random.sample(list(Posts.objects.filter
                                             (is_published=True)),
                                        count_post if count_post < 6 else 6)
            context['blogs'] = blog_6_post
            return context
