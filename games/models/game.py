from django.db import models


class Game(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20, unique=True, null=False, blank=False, db_index=True)
    creation_date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
