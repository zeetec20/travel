from django.views.generic.base import TemplateView
from django.utils import timezone

from destination.models import Country, Destination
from blog.models import Blog
from users.models import Testimoni

class Index(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = 'Home'
        context['homeActive'] = 'active'
        context['listCountry'] = Country.objects.all().order_by('name')
        context['listDestination'] = Destination.objects.all().order_by('-dateCreate')
        context['listTestimoni'] = Testimoni.objects.filter(is_show=True)
        context['listBlog'] = Blog.objects.filter(is_show=True)
        context['timezone_days3'] = timezone.now() - timezone.timedelta(days=3)
        return context