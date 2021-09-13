from django.contrib.auth.models import User
from django.db import models


def avatar_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatars/<user_id>/<filename>
    return f"avatars/{instance.user.pk}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name="用户", on_delete=models.CASCADE
    )
    bio = models.TextField("个人简介", null=True, blank=True)
    avatar = models.ImageField("头像", upload_to=avatar_directory_path)
