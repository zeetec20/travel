from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.utils import timezone

from destination.models import Country
from .models import Blog, BlogLike
from .forms import BlogLikeForm

class Index(TemplateView):
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        context = {
            'place': 'Blog',
            'blogActive': 'active',
            'listCountry': Country.objects.all().order_by('name'),
            'title_blocks_cover': 'Blog Posts',
        }
        
        if 'username' in kwargs and kwargs['username'] != '':
            try:
                allBlog = Blog.objects.filter(user=get_user_model().objects.get(username=kwargs['username']))
            except:
                context['title_blocks_cover'] = 'Writer Not Found'
                allBlog = Blog.objects.all()
        else:
            allBlog = Blog.objects.all()
        context['listBlog'] = allBlog
        context['listBlogLength'] = len(allBlog)
        context['timezone_days3'] = timezone.now() - timezone.timedelta(days=3)
        return context

class BlogView(TemplateView):
    template_name = 'blog/blogView.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = {
            'form': BlogLikeForm(),
            'place': 'Blog',
            'blogActive': 'active',
            'listCountry': Country.objects.all().order_by('name'),
            'timezone_days3': timezone.now() - timezone.timedelta(days=3), 
        }
        return context
    
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(user=get_user_model().objects.filter(username=kwargs['username'])[0], slug=kwargs['slugify'])
        bloglike = BlogLike.objects.filter().count()
        if not blog.exists():
            return redirect('blog:index')
        context = self.get_context_data(*args, **kwargs)
        context2 = {
            'blog': blog[0],
            'order_blog': blog[0].id_blog,
            'title_blocks_cover': blog[0].title,
            'bloglike': bloglike,
            'like': False
        }
        context.update(context2)
        if request.user.is_authenticated:
            context['order_user'] = request.user.id
            context['like'] = BlogLike.objects.filter(blog=Blog.objects.get(slug=kwargs['slugify']), user=request.user).exists()
        else:
            context['order_user'] = False
        return render(request, self.template_name, context)

