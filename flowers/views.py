from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import flowers
from .permissions import IsOwnerOrReadOnly
from .serializers import flowerserializer


class flowersList(ListCreateAPIView):
    queryset = flowers.objects.all()
    serializer_class = flowerserializer


class flowersDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = flowers.objects.all()
    serializer_class = flowerserializer
