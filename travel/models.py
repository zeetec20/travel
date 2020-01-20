from django.db import models
from django.contrib.auth import get_user_model

from uuid import uuid4

class Subscribe(models.Model):
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_subscribe)
            
        while id in allId:
            id = f'sbr{str(uuid4().int)[:8]}'
        return id
    
    id_subscribe = models.CharField(max_length=11, primary_key=True)
    email = models.CharField(max_length=50)
    dateSubscribe = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def save(self):
        allSubscribe = Subscribe.objects.all()
        if self.id_subscribe == None or self.id_subscribe == '':
            id = f'sbr{str(uuid4().int)[:8]}'
            self.id_subscribe = self.get_id(allSubscribe, id)
        else:
            pass
        super(Subscribe, self).save()
    
    def __str__(self):
        return f'{self.email} | {self.dateSubscribe}'