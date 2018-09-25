from django import template
import time

register = template.Library()

@register.filter
def dealwithtime(t1):
    x = time.localtime(t1)
    t2 = time.strftime('%Y-%m-%d %H:%M:%S',x)
    return t2
