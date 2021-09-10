from django.db import models


class File(models.Model):
    file = models.FileField()

    def __str__(self) -> str:
        return str(self.file)
