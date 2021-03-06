from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(**kwargs):
    user = kwargs["instance"]
    if not hasattr(user, "profile"):
        profile = Profile(user=user)
        profile.save()
