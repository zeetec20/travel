from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import redirect

from image_cropping import ImageCroppingMixin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Testimoni

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (('User'), {
            'fields': (
                'username',
                'fullname',
                'email',
                'number_phone',
                'address'
            ),
        }),
    )
    list_display = (
        'id_user',
        'username',
        'fullname',
        'email',
        'number_phone'
    )
    
class TestimoniAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = (
        'id_testimoni',
    )
    
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/users/testimoni/{obj.id_testimoni}/change/')
    
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Testimoni, TestimoniAdmin)