from django.db import models
from django.shortcuts import redirect
from django.core.files.storage import default_storage

from travel2.settings import BASE_DIR
from image_cropping import ImageRatioField
from uuid import uuid4
from PIL import Image

import os

class Team(models.Model):
    def path_upload(self, filename):
        return f'media/about/Team/{self.id_team}/images/image.jpg'
    
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_team)
            
        while id in allId:
            id = f'tem{str(uuid4().int)[:8]}'
        return id
    
    id_team = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to=path_upload)
    cropping = ImageRatioField('profile', '700x700')
    description = models.TextField()
    dateCreate  = models.DateField(auto_now_add=True, null=True, blank=True)
    dateUpdate  = models.DateField(auto_now=True, null=True, blank=True)
    
    def save(self):
        allTeam = Team.objects.all()
        path = [
            f'media/about/Team/{self.id_team}/images/image.jpg',
            f'media/about/Team/{self.id_team}/images/image.jpg.300x300_q85_detail_upscale.jpg'
        ]
        if self.id_team == None or self.id_team == '':
            id = f'tem{str(uuid4().int)[:8]}'
            self.id_team = self.get_id(allTeam, id)
        else:
            original_image = Image.open(os.path.join(BASE_DIR, path[0]))
            cord = str(self.cropping).split(',')
            image_cropped = original_image.crop((int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])))
            default_storage.delete(path[0])
            image_cropped.save(os.path.join(BASE_DIR, path[0]))
        default_storage.delete(path[1])
        super(Team, self).save()
        
    def delete(self):
        shutil.rmtree(os.path.join(BASE_DIR, f'media/about/Team/{self.id_team}'))
        super(Destination, self).delete()

    def __str__(self):
        return f'{self.id_team} | {self.name}'

class SosmedTeam(models.Model):
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_sosmedTeam)
            
        while id in allId:
            id = f'stm{str(uuid4().int)[:8]}'
        return id
    
    sosmed_choices = (
        ('telegram', 'Telegram'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'Whatsapp'),
        ('twitter', 'Twitter')
    )
    
    id_sosmedTeam = models.CharField(max_length=11)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=9, choices=sosmed_choices)
    link = models.URLField()
    
    def save(self):
        allSosmedTeam = SosmedTeam.objects.all()
        if self.id_sosmedTeam == None or self.id_sosmedTeam == '':
            id = f'stm{str(uuid4().int)[:8]}'
            self.id_sosmedTeam = self.get_id(allSosmedTeam, id)
        else:
            pass
        if not SosmedTeam.objects.filter(team=self.team, name=self.name).exists():
            super(SosmedTeam, self).save()
    
    def __str__(self):
        return f'{self.team.name} | {self.name}'