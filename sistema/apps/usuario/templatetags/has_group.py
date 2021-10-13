from django import template

register = template.Library()

@register.filter(name = 'has_group')
def has_group(usuario,rol):
    return usuario.groups.filter(name__exact = rol).exists()
