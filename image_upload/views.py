from PIL import Image as PILImage
from django.http import HttpResponseBadRequest
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


class ImageUploadView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        tier = user.userprofile.tier

        if not tier:
            return HttpResponseBadRequest("User tier not specified.")

        image_file = self.request.data.get('image')

        if not image_file:
            return HttpResponseBadRequest("Image not provided.")

        image_instance = serializer.save(user=user)

    def generate_thumbnail(self, image_instance, size):
        try:
            # Otwórz oryginalny obraz
            image = PILImage.open(image_instance.image)

            # Ustaw szerokość/proporcje na podstawie żądanej wielkości
            width = size
            height = int((float(image.size[1]) / float(image.size[0])) * float(width))
            new_size = (width, height)

            # Wygeneruj miniaturę
            image.thumbnail(new_size, PILImage.ANTIALIAS)

            # Zapisz miniaturę w polu Miniatura modelu Image
            image_instance.thumbnail = image

            # Zapisz model Image z miniaturą
            image_instance.save()

        except Exception as e:
            print(f"Error generating thumbnail: {str(e)}")
