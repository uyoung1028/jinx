from django import template

register = template.Library()

@register.filter
def find_category(category, name):
    return category.get(name=name).noun_set.all()