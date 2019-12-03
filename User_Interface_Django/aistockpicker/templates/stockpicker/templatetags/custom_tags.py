from django import template

register = template.Library()


@register.custom_tags
def mult(a, b):
    return a*b