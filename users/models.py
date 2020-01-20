from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage

from PIL import Image
from image_cropping import ImageRatioField, ImageCropField
from uuid import uuid4
from travel2.settings import BASE_DIR

import os

class CustomUser(AbstractUser):
    id_user = models.IntegerField()
    fullname = models.CharField(max_length = 50, default='')
    number_phone = models.IntegerField(default=0)
    address = models.TextField(default='')
    gender = models.CharField(default='o', max_length=1)
    customer = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.id_user == None or self.id_user == '':
            self.id_user = int(str(uuid4().int)[:8])
            if self.is_staff:
                self.customer = False
            if self.is_superuser:
                self.is_staff = True
        else:
            pass
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id_user} | {self.username}"

class Testimoni(models.Model):
    def path_upload(self, filename):
        return f'media/user/Testimoni/{self.id_testimoni}/images/image.jpg'
    
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_testimoni)
            
        while id in allId:
            id = f'tst{str(uuid4().int)[:8]}'
        return id

    id_testimoni = models.CharField(max_length=11, primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    is_show = models.BooleanField(default=False)
    cover = ImageCropField(upload_to=path_upload)
    cropping = ImageRatioField('cover', '700x800')

    def save(self):
        allTestimoni = Testimoni.objects.all()
        path = [
            f'media/user/Testimoni/{self.id_testimoni}/images/image.jpg', 
            f'media/user/Testimoni/{self.id_testimoni}/images/image.jpg.300x300_q85_detail_upscale.jpg'
        ]
        if self.id_testimoni == None or self.id_testimoni == '':
            id = f'tst{str(uuid4().int)[:8]}'
            self.id_testimoni = self.get_id(allTestimoni, id)
        else:
            original_image = Image.open(os.path.join(BASE_DIR, path[0]))
            cord = str(self.cropping).split(',')
            image_cropped = original_image.crop((int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])))
            default_storage.delete(path[0])
            image_cropped.save(os.path.join(BASE_DIR, path[0]))
        default_storage.delete(path[1])
        super(Testimoni, self).save()
    
    def __str__(self):
        return f'{self.user.fullname} - {self.user.username}'
