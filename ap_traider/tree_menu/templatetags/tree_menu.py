from django import template
from django.urls import resolve

from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("tree_menu/template_tags/menu.html", takes_context=True)
def show_menu(context, menu_name):
    current_url = resolve(context.request.path_info).url_name
    menu_items = MenuItem.objects.filter(name=menu_name)
    return {
        "menu_items": menu_items,
        "current_url": current_url,
        "request": context.request,
    }


@register.inclusion_tag("tree_menu/template_tags/children.html", takes_context=True)
def show_children(context, parent_name):
    current_name = resolve(context.request.path_info).url_name
    children = MenuItem.objects.prefetch_related("children").filter(
        parent__name=parent_name
    )
    return {
        "request": context.request,
        "children": children,
        "current_url": current_name,
    }
