from django.urls import path
from .views_front import (
    flowersCreateView,
    flowersDeleteView,
    flowersDetailView,
    flowersListView,
    flowersUpdateView,
)

urlpatterns = [
    path("", flowersListView.as_view(), name="flowers_list"),
    path("<int:pk>/", flowersDetailView.as_view(), name="flowers_detail"),
    path("create/", flowersCreateView.as_view(), name="flowers_create"),
    path("<int:pk>/update/", flowersUpdateView.as_view(), name="flowers_update"),
    path("<int:pk>/delete/", flowersDeleteView.as_view(), name="flowers_delete"),
]
