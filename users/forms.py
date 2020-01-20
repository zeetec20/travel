from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from image_cropping import ImageCropWidget
from .models import CustomUser, Testimoni

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'number_phone',
            'address'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'number_phone',
            'address'
        )

class RegisterForm(forms.ModelForm):
    class Meta:
        model   = CustomUser
        fields  = (
            'fullname',
            'username',
            'email',
            'number_phone',
            'password',
            'gender',
            'address'
        )
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = (
            'user',
            'cover',
            'text',
        )
        
        widgets = {
            'cover': ImageCropWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'text': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'cols': '30',
                    'rows': '5',
                    'placeholder': 'Write your testimoni...'
                }
            )
        }