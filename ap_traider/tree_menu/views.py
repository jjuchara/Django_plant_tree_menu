from django.views.generic import DetailView, TemplateView

from tree_menu.models import MenuItem


class NavTreeView(TemplateView):
    template_name = "tree_menu/home.html"


class NavItemDetailView(DetailView):
    model = MenuItem
    template_name = "tree_menu/menu-item-detail.html"
    context_object_name = "item"
    slug_field = "url"
