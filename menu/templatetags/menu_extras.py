from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Возращаем элемент из словаря для обработки в HTML"""
    return dictionary.get(key)
