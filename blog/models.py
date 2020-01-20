from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.utils.text import slugify

from travel2.settings import BASE_DIR
from image_cropping import ImageCropField, ImageRatioField
from uuid import uuid4
from PIL import Image

import os

class Blog(models.Model):
    def path_upload(self, filename):
        return f'media/blog/Blog/{self.id_blog}/images/image.jpg'
    
    def get_id(self, allObject, id):
        allId = allObject.values_list('id_blog', flat=True)
            
        while id in allId:
            id = f'blg{str(uuid4().int)[:8]}'
        return id
    
    id_blog = models.CharField(max_length=11, primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    cover = ImageCropField(upload_to=path_upload)
    cropping = ImageRatioField('cover', '1900x1267')
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_show = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    
    def save(self):
        allBlog = Blog.objects.all()
        path = [
            f'media/blog/Blog/{self.id_blog}/images/image.jpg', 
            f'media/blog/Blog/{self.id_blog}/images/image.jpg.300x300_q85_detail_upscale.jpg'
        ]
        
        if self.id_blog == '' or self.id_blog == None:
            id = f'blg{str(uuid4().int)[:8]}'
            self.id_blog = self.get_id(allBlog, id)
        else:
            original_image = Image.open(os.path.join(BASE_DIR, path[0]))
            cord = str(self.cropping).split(',')
            image_cropped = original_image.crop((int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])))
            default_storage.delete(path[0])
            image_cropped.save(os.path.join(BASE_DIR, path[0]))
        self.slug = slugify(self.title)
        default_storage.delete(path[1])
        super(Blog, self).save()
    
    def __str__(self):
        return f'{self.user.username} | {self.title}'

class BlogLike(models.Model):
    def get_id(self, allObject, id):
        allId = allObject.values_list('id_bloglike', flat=True)
            
        while id in allId:
            id = f'blk{str(uuid4().int)[:8]}'
        return id
    
    id_bloglike = models.CharField(max_length=11, primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def save(self):
        allBlogLike = BlogLike.objects.all()
        
        if self.id_bloglike == '' or self.id_bloglike == None:
            id = f'blk{str(uuid4().int)[:8]}'
            self.id_bloglike = self.get_id(allBlogLike, id)
        else:
            pass
        
        if not BlogLike.objects.filter(user=self.user, blog=self.blog).exists():
            super(BlogLike, self).save()
