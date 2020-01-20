from django.contrib import admin
from django.shortcuts import redirect

from image_cropping import ImageCroppingMixin

from .models import Team, SosmedTeam

class TeamAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = (
        'id_team',
    )
    
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/about/team/{obj.id_team}/change/')
    
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

class SosmedTeamAdmin(admin.ModelAdmin):
    exclude = (
        'id_sosmedTeam',
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(SosmedTeam, SosmedTeamAdmin)