from django.contrib import admin
from image_cropping import ImageCroppingMixin
from django.shortcuts import redirect

from .models import Country, Destination, Lodging

class DestinationAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = (
        'id_destination',
    )
    
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/destination/destination/{obj.id_destination}/change/')
    
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

class LodgingAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = (
        'id_lodging',
    )
    
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/destination/lodging/{obj.id_lodging}/change/')
    
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

admin.site.register(Country)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Lodging, LodgingAdmin)
