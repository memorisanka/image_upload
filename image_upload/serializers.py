from rest_framework import serializers
from .models import Tier, Image


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ('name', 'thumbnail_sizes', 'allow_original_link', 'allow_expiring_link')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('user', 'image', 'tier', 'created_at', 'updated_at')
