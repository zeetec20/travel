from django.contrib.auth import get_user_model, authenticate, login, logout

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from travel.models import Subscribe
from users.forms import RegisterForm, LoginForm, TestimoniForm
from users.models import Testimoni
from blog.forms import BlogForm
from contact.forms import MessageForm
from blog.forms import BlogLikeForm
from blog.models import Blog, BlogLike

class APIToken(APIView):
    def get(self, request, *args, **kwargs):
        if 'username' in request.GET and 'password' in request.GET and get_user_model().objects.filter(username=request.GET['username']).exists():
            if 'password' in request.GET:
                user = authenticate(request, username=request.GET['username'], password=request.GET['password'])
                if user is not None:
                    token = Token.objects.get_or_create(user=user)
                    response = {
                        'success': 'true',
                        'message': f'{user.username} | Token: {token[0].key}'
                    }
                else:
                    response = {
                        'success': 'false',
                        'message': f'username or password invalid'
                    }
        else:
            response = {
                'success': 'false',
                'message': f'User not found'
            }
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        if 'username' in request.POST and 'password' in request.POST and get_user_model().objects.filter(username=request.POST['username']).exists():
            if 'password' in request.POST:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    token = Token.objects.get_or_create(user=user)
                    response = {
                        'success': 'true',
                        'message': f'{user.username} | Token: {token[0].key}'
                    }
                else:
                    response = {
                        'success': 'false',
                        'message': f'username or password invalid'
                    }
        else:
            response = {
                'success': 'false',
                'message': f'User not found'
            }
        return Response(response)

class APISubscribe(APIView):
    def post(self, request, *args, **kwargs):
        if 'email' in request.POST:
            subscribe = Subscribe(email=request.POST['email'])
            subscribe.save()
            response = {
                'success': 'true',
                'message': 'Thanks for subscribe'
            }
        else:
            response = {
                'success': 'false',
                'message': 'Not found email'
            }
        return Response(response)

class APILogout(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        response = {
            'success': 'true',
            'message': f'Succesful logout {user.username}'
        }
        return Response(response)

class APIRegister(APIView):
    def post(self, request, *args, **kwargs):
        # request.POST['gender'] = int(request.POST['gender'])
        print(request.POST)
        formRegister = RegisterForm(request.POST or None)
        if formRegister.is_valid():
            formRegister.save()
            response = {
                'success': 'true',
                'message': f'New User: {request.POST["username"]}'
            }
        else:
            response = {
                'success': 'false',
                'message': 'Failed Create New User'
            }
        return Response(response)

class APILogin(APIView):
    def post(self, request, *args, **kwargs):
        formLogin = LoginForm(request.POST or None)
        if formLogin.is_valid():
            username = formLogin.cleaned_data.get('username')
            password = formLogin.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                index = 0
                order_user = 0
                for user in get_user_model().objects.all():
                    index += 1
                    if user.username == request.user.username:
                        order_user = index
                response = {
                    'success': 'true',
                    'message': 'Successful login',
                    'order_user': order_user,
                    'user': f'{username}'
                }
            else:
                response = {
                    'success': 'false',
                    'message': 'Username or password incorect',
                }
        else:
            print(formLogin.errors)
            response = {
                'success': 'false',
                'message': 'Failed login'
            }
        return Response(response)

class APIMessage(APIView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
            response = {
                'success': 'true',
                'message': 'Successful send message'
            }
            return Response(response)
        else:
            response = {
                'success': 'false',
                'message': 'Failed send message'
            }
            return Response(response)

class APITestimoni(APIView):
    def post(self, request, *args, **kwargs):
        form = TestimoniForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            response = {
                'success': 'true',
                'message': 'Success send testimoni'
            }
        else:
            response = {
                'success': 'false',
                'message': 'Failed send testimoni'
            }
        return Response(response)

class APIBlog(APIView):
    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            response = {
                'success': 'true',
                'message': 'Success write blog'
            }
        else:
            response = {
                'success': 'false',
                'message': 'Failed write blog'
            }
        return Response(response)

class APIBlogLike(APIView):
    def post(self, request, *args, **kwargs):
        form = BlogLikeForm(request.POST)
        if form.is_valid():
            form.save()
            blog = Blog.objects.get(id_blog=request.POST['blog'])
            response = {
                'success': 'true',
                'message': f'Success liked, blog : \"{blog.title}\"'
            }
        else:
            response = {
                'success': 'false',
                'message': 'Failed liked blog'
            }
        return Response(response)

class APIBlogUnlike(APIView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        id = request.POST['id_user']
        slug = request.POST['slugify']
        user = get_user_model().objects.get(id_user=id)
        blog = Blog.objects.get(slug=slug)
        like = BlogLike.objects.get(user=user, blog=blog)
        like.delete()
        response = {
            'success': 'true',
            'message': f'Success unliked, blog : \"{blog.title}\"'
        }
        return Response(response)

class APICsrfToken(APIView):
    pass