from django.db import models


class Announcement(models.Model):
    title = models.CharField(verbose_name='Title', blank=False, null=False, db_index=True, max_length=40)
    text = models.TextField(verbose_name='Text', blank=False, null=False)

    STATE_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    state = models.CharField(verbose_name='State', choices=STATE_CHOICES, max_length=1)

    creation_date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)
    expire_date = models.DateTimeField(verbose_name='Expiration Date', blank=True, null=True)
