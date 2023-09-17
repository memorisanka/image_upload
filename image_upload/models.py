from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField


class Tier(models.Model):
    name = models.CharField(max_length=255)
    thumbnail_sizes = JSONField(default=list)
    allow_original_link = models.BooleanField(default=False)
    allow_expiring_link = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user} Profile'
