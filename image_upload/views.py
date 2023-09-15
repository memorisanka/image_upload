from rest_framework import generics
from rest_framework import permissions

from .models import Image
from .serializers import ImageSerializer


class ImageView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)
