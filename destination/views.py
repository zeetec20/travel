from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from destination.models import (
    Country, 
    Destination,
    Lodging
)
from users.models import Testimoni

class Index(TemplateView):
    template_name = 'destination/index.html'
    
    def get(self, request, *args, **kwargs):
        if 'country' in kwargs and not Country.objects.filter(name=kwargs['country'].upper()).exists():
            return redirect('destination:index')
        return render(self.request, self.template_name, self.get_context_data())
    
    def get_context_data(self, **kwargs):
        context = {
            'destinationActive': 'active',
            'listCountry': Country.objects.all().order_by('name'),
            'listTestimoni': Testimoni.objects.filter(is_show=True),
            'country': None,
            'place': 'Destinations',
            'title_blocks_cover': 'Destinations'
        }
        
        if 'country' in kwargs and kwargs['country'] != None:
            context['country'] = kwargs['country']
            country = Country.objects.get(name=kwargs['country'].upper())
            context['listDestination'] = Destination.objects.filter(country=country)
        else:
            context['listDestination'] = Destination.objects.all()
            context['country'] = None
        return context
    
class DestinationDetail(TemplateView):
    template_name = 'destination/destinationDetail.html'

    def get(self, request, *args, **kwargs):
        if not Destination.objects.filter(country=Country.objects.get(name=kwargs['country'].upper()), slug=kwargs['name']).exists():
            return redirect('destination:index')
        
        destination = Destination.objects.get(country=Country.objects.get(name=kwargs['country'].upper()), slug=kwargs['name'])
        context = self.get_context_data()
        context['destination'] = destination
        context['title_blocks_cover'] = destination.name
        print(len(Lodging.objects.filter(destination=destination)))
        context['listLodging'] = Lodging.objects.filter(destination=destination)
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        
        context = {
            'place': 'Destination',
            'destinationActive': 'active',
            'listCountry': Country.objects.all().order_by('name'),
        }
        return context
    