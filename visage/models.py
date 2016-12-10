from django.contrib.auth.models import User
from django.db import models


class Announcement(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Author', blank=False, null=False, db_index=True, limit_choices_to={'is_staff': True}
    )
    title = models.CharField(verbose_name='Title', blank=False, null=False, db_index=True, max_length=40)
    text = models.TextField(verbose_name='Text', blank=False, null=False)

    STATE_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    state = models.CharField(verbose_name='State', choices=STATE_CHOICES, max_length=1)

    creation_date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)
