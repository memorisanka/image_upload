from django.contrib.auth.models import User
from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=255)
    thumbnail_sizes = models.CharField(max_length=255)
    allow_original_link = models.BooleanField(default=False)
    allow_expiring_link = models.BooleanField(default=False)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)