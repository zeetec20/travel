from django.urls import path

from .views import Index, BlogView

app_name='blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:username>/', Index.as_view(), name='blog-username'),
    path('<str:username>/<str:slugify>/', BlogView.as_view(), name='blog-username-detail')
]
