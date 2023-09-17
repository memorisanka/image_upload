import os

from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile, Tier


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()


@receiver(post_migrate)
def create_builtin_plans(sender, **kwargs):
    if sender.name == 'image_upload' and not os.environ.get('BUILTIN_PLANS_CREATED'):
        Tier.objects.get_or_create(name="Basic", thumbnail_sizes=[200], )
        Tier.objects.get_or_create(name="Premium", thumbnail_sizes=[200, 400], allow_original_link=True)
        Tier.objects.get_or_create(name="Enterprise", thumbnail_sizes=[200, 400], allow_original_link=True,
                                   allow_expiring_link=True)
        os.environ['BUILTIN_PLANS_CREATED'] = 'True'
