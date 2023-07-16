from django import template

register = template.Library()


@register.simple_tag
def to_class_name(object):
    return str(object.__class__.__name__)
