from django.urls import path
from .views import ImageUploadView, ImageView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('images/', ImageView.as_view(), name='image-list'),
]