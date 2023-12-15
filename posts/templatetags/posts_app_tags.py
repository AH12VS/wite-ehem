from django import template

PER_CHARSET = ('','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',)

register = template.Library()

@register.simple_tag()
def check_tag_slug():
    pass

