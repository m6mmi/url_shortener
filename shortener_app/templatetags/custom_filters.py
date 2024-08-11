# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_field(obj, field_name):
    return getattr(obj, field_name, None)


@register.filter
def attr(obj, attr):
    return getattr(obj, attr)

@register.simple_tag
def get_attr(obj, attr):
    return getattr(obj, attr)