from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("items", views.search, name="search"),
    path("items/<int:item_id>", views.show, name="show")
]