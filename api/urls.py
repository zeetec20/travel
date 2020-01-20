from django.urls import path
from .views import (
    APIToken, 
    APISubscribe, 
    APIRegister, 
    APILogin,
    APILogout,
    APITestimoni,
    APIMessage,
    APIBlog,
    APIBlogLike,
    APIBlogUnlike
)

app_name='api'
urlpatterns = [
    path('token', APIToken.as_view(), name='token'),
    path('subscribe', APISubscribe.as_view(), name='subscribe'),
    path('user/register', APIRegister.as_view(), name='register'),
    path('user/login', APILogin.as_view(), name='login'),
    path('user/logout', APILogout.as_view(), name='logout'),
    path('user/testimoni', APITestimoni.as_view(), name='testimoni'),
    path('blog/write', APIBlog.as_view(), name='blog'),
    path('blog/like', APIBlogLike.as_view(), name='blog_like'),
    path('blog/unlike', APIBlogUnlike.as_view(), name='blog_unlike'),
    path('message', APIMessage.as_view(), name='message'),
]

