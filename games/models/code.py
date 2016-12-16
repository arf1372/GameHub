import os

from django.db import models
from django.conf import settings

from profiles.models import Team


def upload_path(*args, **kwargs):
    return os.path.join(settings.BASE_DIR, 'uploaded/codes/')


class Code(models.Model):
    team = models.ForeignKey(Team, verbose_name='Team', null=False, blank=False)

    # TODO: Check these later!
    LANGUAGE_CHOICES = (
        ('c', 'C'),
        ('cpp98', 'C++98'),
        ('cpp11', 'C++11'),
        ('cpp14', 'C++14'),
        ('java7', 'Java 7'),
        ('java8', 'Java 8'),
        ('py2', 'Python 2'),
        ('py3', 'Python 3'),
    )
    language = models.CharField(verbose_name='Language', choices=LANGUAGE_CHOICES, max_length=5)

    file = models.FileField(verbose_name='File', upload_to=upload_path, null=False, blank=False)
    upload_date = models.DateTimeField(verbose_name='Upload Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'
