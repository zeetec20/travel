from django.contrib import admin
from .models import Subscribe

class AdminSubscribe(admin.ModelAdmin):
    exclude = (
        'id_subscribe',
    )

admin.site.register(Subscribe, AdminSubscribe)