from django import template
from recipe_app.main.models import Recipe

register = template.Library()


@register.simple_tag
def get_first_recipe():
    return Recipe.objects.first()
