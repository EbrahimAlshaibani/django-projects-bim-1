from django import template
from store.models import Setting

register = template.Library()

@register.filter
def myTheme():
    return Setting.objects.get(key="theme")
