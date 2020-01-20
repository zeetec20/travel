from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

from destination.models import Country
from blog.forms import BlogForm
from .forms import TestimoniForm, Testimoni

class Index(View):
    template_name = 'user/index.html'
    context = {
        'listCountry': Country.objects.all().order_by('name'),
        'userActive': 'active',
        'place': 'User',
        'formTestimoni': TestimoniForm(),
        'formBlog': BlogForm(),
        'order_user': False,
        'title_blocks_cover': [
            'Register Your Self',
            'Enjoy Your Trip'
        ]
    }
    
    def get(self, request):
        index = 0
        if request.user.is_authenticated:
            for user in get_user_model().objects.all():
                index += 1
                if user.username == request.user.username:
                    self.context['order_user'] = index
        return render(self.request, self.template_name, self.context)
