from django.views.generic import TemplateView

from destination.models import Country
from users.models import Testimoni
from .models import Team, SosmedTeam

class Index(TemplateView):
    template_name='about/index.html'
    
    def get_context_data(self, **kwargs):
        allTeam = Team.objects.all()
        context = super().get_context_data(**kwargs)
        context['listTeam'] = allTeam
        context['place'] = 'About'
        context['aboutActive'] = 'active'
        context['listCountry'] = Country.objects.all().order_by('name')
        context['listTestimoni'] = Testimoni.objects.filter(is_show=True)
        context['title_blocks_cover'] = 'About ZeeTrav'
        sosmed = []
        for team in allTeam:
            sosmed.append([SosmedTeam.objects.filter(team=team).order_by('name')])
        context['listSosmed'] = sosmed
        return context
    