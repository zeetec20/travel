from django.contrib import admin

from image_cropping import ImageCroppingMixin
from .models import Blog, BlogLike

class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = (
        'id_blog',
    )

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogLike)