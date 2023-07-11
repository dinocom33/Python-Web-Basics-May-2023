from django import template
from fruitipedia_app.web.models import ProfileModel

register = template.Library()


@register.simple_tag
def get_user_profile():
    return ProfileModel.objects.first()
