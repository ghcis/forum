from django.db import models

from django.contrib.auth.models import User


class Thread(models.Model):
    title = models.CharField("标题", max_length=128)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="用户", null=True
    )

    def __str__(self) -> str:
        return str(self.title)


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="用户", null=True
    )
    pub_date = models.DateTimeField("发布日期")
    relpy_to = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="回复", blank=True, null=True
    )
    content = models.TextField("内容")
