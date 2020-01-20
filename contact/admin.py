from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    exclude = (
        'id_message',
    )

admin.site.register(Message, MessageAdmin)