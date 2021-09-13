from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name="用户", on_delete=models.CASCADE
    )
    bio = models.TextField("个人简介", null=True, blank=True)
