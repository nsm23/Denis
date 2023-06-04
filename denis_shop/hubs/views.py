from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from hubs.models import Category


# Create your views here.
class HubView(ListView):
    template_name = 'hub/index.html'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get('category_slug')
        hub = get_object_or_404(Category, slug=slug)
        self.extra_context = {
            'page_title': f'Категории | {hub}',
            'current_hub': slug
        }
        return Category.objects.filter(Q(slug))

