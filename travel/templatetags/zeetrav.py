from django import template
from django.utils import timezone

register = template.Library()

def convertLocalTime(value):
    local_time = timezone.localtime(value)
    print(timezone.now())
    print(timezone.now() - timezone.timedelta(days=2))
    print(timezone.now() > timezone.now() - timezone.timedelta(days=2))
    return local_time

register.filter('localtime', convertLocalTime)

def newestBlog(value):
    test = timezone.now() - timezone.timedelta(days=3)
    value = (value > test)
    return value


register.filter('newblog', newestBlog)