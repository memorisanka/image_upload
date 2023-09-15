from django.contrib.auth.models import User
from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=255)
    thumbnail_sizes = models.CharField(max_length=255)
    allow_original_link = models.BooleanField(default=False)
    allow_expiring_link = models.BooleanField(default=False)
