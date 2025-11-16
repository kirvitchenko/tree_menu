from django import template
from django.urls import reverse, NoReverseMatch

from menu.models import MenuItem


def find_active_item(items, request):
    """Находим активный элемент меню исходя из URL"""
    item = None
    for i in items:
        try:
            named_url = reverse(i.named_url) if i.named_url else None
        except NoReverseMatch:
            named_url = None

        if i.url == request.path or named_url == request.path:
            item = i
            break
    return item


def find_parents(item):
    """Ищем родителей вверх по дереву для того чтобы соблюсти правильную вложенность"""
    parents_list = []
    current = item
    while current.parent is not None:
        parents_list.append(current.parent)
        current = current.parent
    return parents_list


register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    """
    Создаем дерево элементов меню на основе связи parent-child
    Отмечаем активный пункт и те пункты которые должны быть развернуты
    """
    request = context["request"]
    items = MenuItem.objects.filter(menu__name=menu_name).order_by("parent_id", "order")

    active_item = find_active_item(items, request)

    if active_item is None:
        return {"items": {}}

    parents_list = find_parents(active_item)

    tag_dict = {}

    for item in items:
        tag_dict[item.id] = {
            "item": item,
            "children": [],
            "is_active": False,
            "is_expanded": False,
        }
    for i in items:
        if i.parent:
            tag_dict[i.parent.id]["children"].append(i.id)

    tag_dict[active_item.id]["is_active"] = True
    tag_dict[active_item.id]["is_expanded"] = True

    for p in parents_list:
        tag_dict[p.id]["is_expanded"] = True

    for c in tag_dict[active_item.id]["children"]:
        tag_dict[c]["is_expanded"] = True

    return {"items": tag_dict}
