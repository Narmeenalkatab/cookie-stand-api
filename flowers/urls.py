from django.urls import path
from .views import flowersList, flowersDetail

urlpatterns = [
    path("", flowersList.as_view(), name="flowers_list"),
    path("<int:pk>/", flowersDetail.as_view(), name="flowers_detail"),
]
