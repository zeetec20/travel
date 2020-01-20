from django.db import models
from uuid import uuid4

class Message(models.Model):
    def get_id(self, allObject, id):
        allId = []
        for obj in allObject:
            allId.append(obj.id_message)
            
        while id in allId:
            id = f'msg{str(uuid4().int)[:8]}'
        return id
    
    id_message  = models.CharField(max_length=11, primary_key=True)
    
    fullname    = models.CharField(max_length=50)
    email       = models.EmailField()
    subject     = models.CharField(max_length=30)
    message     = models.TextField()
    
    def save(self):
        allMessage = Message.objects.all()
        if self.id_message == None or self.id_message == '':
            id = f'msg{str(uuid4().int)[:8]}'
            self.id_message = self.get_id(allMessage, id)
        else:
            pass
        super(Message, self).save()
    
    def __str__(self):
        return f'{self.fullname} | {self.email} | {self.subject}'
    