from django.urls import path

from .views import NavItemDetailView, NavTreeView

urlpatterns = [
    path("", NavTreeView.as_view(), name="home"),
    path("<slug:slug>", NavItemDetailView.as_view(), name="detail"),
]
