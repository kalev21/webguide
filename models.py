from django.db import models


class FolderModel(models.Model):
    name = models.TextField('Название папки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название папки'
        verbose_name_plural = 'Название папок'


