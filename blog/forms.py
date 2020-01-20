from django import forms

from image_cropping import ImageCropWidget
from .models import Blog, BlogLike

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'user',
            'cover',
            'title',
            'content'
        )
        widgets = {
            'user': forms.TextInput(
                attrs = {
                    'id': 'id_user_blog',
                }
            ),
            'cover': ImageCropWidget(
                attrs = {
                    'id': 'id_cover_blog',
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'id': 'id_title_blog',
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'id': 'id_content_blog',
                    'class': 'form-control',
                    'placeholder': 'Write your blog...'
                }
            )
        }

class BlogLikeForm(forms.ModelForm):
    class Meta:
        model = BlogLike
        fields = (
            'blog',
            'user',
        )
        widgets = {
            'user': forms.Select(
                attrs={
                    'required':'false'
                }
            )
        }