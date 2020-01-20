from django.db import models
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.utils.text import slugify

from travel2.settings import BASE_DIR
from image_cropping import ImageRatioField
from uuid import uuid4
from PIL import Image

import os,shutil

class Country(models.Model):
    id_country = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=25)
    
    def save(self):
        self.id_country = self.id_country.upper()
        self.name = self.name.upper()
        super(Country, self).save()
    
    def __str__(self):
        return f'{self.name}'


class Destination(models.Model):
    def path_upload1(self, filename):
        return f'media/destination/Destination/{self.id_destination}/images/cover.jpg'
    
    def path_upload2(self, filename):
        return f'media/destination/Destination/{self.id_destination}/images/image.jpg'
    
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_destination)
            
        while id in allId:
            id = f'dst{str(uuid4().int)[:8]}'
        return id
    
    description_default = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vitae cumque eius modi expedita accusamus alias error totam ab magnam a mollitia magni, distinctio temporibus optio illo sapiente, odio unde natus.'
    
    id_destination = models.CharField(max_length=11, primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    cover = models.ImageField(upload_to=path_upload1)
    profile = models.ImageField(upload_to=path_upload2)
    croppingCover = ImageRatioField('cover', '1900x1267')
    croppingProfile = ImageRatioField('profile', '700x800')
    price = models.IntegerField()
    description = models.TextField(default=description_default)
    slug = models.SlugField(null=True, blank=True)
    dateCreate  = models.DateField(auto_now_add=True, null=True, blank=True)
    dateUpdate  = models.DateField(auto_now=True, null=True, blank=True)
    
    def save(self):
        allDestination = Destination.objects.all()
        path = [
            f'media/destination/Destination/{self.id_destination}/images/image.jpg', 
            f'media/destination/Destination/{self.id_destination}/images/image.jpg.300x300_q85_detail_upscale.jpg'
        ]
        path2 = [
            f'media/destination/Destination/{self.id_destination}/images/cover.jpg', 
            f'media/destination/Destination/{self.id_destination}/images/cover.jpg.300x300_q85_detail_upscale.jpg'
        ]
        if self.id_destination == None or self.id_destination == '':
            id = f'dst{str(uuid4().int)[:8]}'
            self.id_destination = self.get_id(allDestination, id)
        else:
            original_image = Image.open(os.path.join(BASE_DIR, path[0]))
            cord = str(self.croppingProfile).split(',')
            print(cord)
            image_cropped = original_image.crop((int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])))
            default_storage.delete(path[0])
            image_cropped.save(os.path.join(BASE_DIR, path[0]))
            
            original_image2 = Image.open(os.path.join(BASE_DIR, path2[0]))
            cord2 = str(self.croppingCover).split(',')
            print(cord2)
            image_cropped = original_image.crop((int(cord2[0]), int(cord2[1]), int(cord2[2]), int(cord2[3])))
            default_storage.delete(path2[0])
            image_cropped.save(os.path.join(BASE_DIR, path2[0]))
        if (self.slug == '' or self.slug == None) and Destination.objects.filter(slug=slugify(self.name)):
            self.slug = f'{slugify(self.name)}-{str(uuid4())[:8]}'
        elif self.slug == '' or self.slug == None:
            self.slug = slugify(self.name)
        default_storage.delete(path[1])
        super(Destination, self).save()
    
    def delete(self):
        shutil.rmtree(os.path.join(BASE_DIR, f'media/destination/Destination/{self.id_destination}'))
        super(Destination, self).delete()
    
    def __str__(self):
        return f'{self.country.name.lower().capitalize()} | {self.name}'


class Lodging(models.Model):
    def path_upload(self, filename):
        return f'media/destination/Lodging/{self.id_lodging}/images/image.jpg'
    
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_lodging)
            
        while id in allId:
            id = f'lgng{str(uuid4().int)[:8]}'
        return id
    
    id_lodging = models.CharField(max_length=12, primary_key=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=path_upload)
    cropping = ImageRatioField('image', '700x800')
    price = models.IntegerField()
    address = models.TextField()
    website = models.URLField(null=True, blank=True)
    postalCode = models.IntegerField()
    
    def save(self):
        allLodging = Lodging.objects.all()
        path = [
            f'media/destination/Lodging/{self.id_lodging}/images/image.jpg', 
            f'media/destination/Lodging/{self.id_lodging}/images/image.jpg.300x300_q85_detail_upscale.jpg'
        ]
        if self.id_lodging == None or self.id_lodging == '':
            id = f'lgng{str(uuid4().int)[:8]}'
            self.id_lodging = self.get_id(allLodging, id)
        else:
            original_image = Image.open(os.path.join(BASE_DIR, path[0]))
            cord = str(self.cropping).split(',')
            print(cord)
            image_cropped = original_image.crop((int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])))
            default_storage.delete(path[0])
            image_cropped.save(os.path.join(BASE_DIR, path[0]))
        default_storage.delete(path[1])
        super(Lodging, self).save()

    def delete(self):
        shutil.rmtree(os.path.join(BASE_DIR, f'media/destination/Lodging/{self.id_lodging}'))
        super(Lodging, self).delete()
    
    def __str__(self):
        return f'{self.name} | {self.postalCode}'

# class PacketDestination(models.Model):
#     pass