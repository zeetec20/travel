from django.views.generic import TemplateView

from destination.models import Country

class Index(TemplateView):
    template_name = 'contact/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contactActive"] = 'active'
        context['listCountry'] = Country.objects.all().order_by('name')
        context['place'] = 'Contact'
        context['title_blocks_cover'] = 'Get in Touch'
        return context
    