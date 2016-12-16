import os

from django.db import models
from django.conf import settings

from games.models.game import Game
from profiles.models import Team


def upload_path(*args, **kwargs):
    return os.path.join(settings.BASE_DIR, 'uploaded/codes/')


class Match(models.Model):
    game = models.ForeignKey(Game, verbose_name='Game')
    teams = models.ManyToManyField(Team, verbose_name='Team', through='TeamMatch', through_fields=('match', 'team'))
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    result = models.FileField(verbose_name='Result', upload_to=upload_path, null=False, blank=False)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'


class TeamMatch(models.Model):
    match = models.ForeignKey(Match, verbose_name='Match')
    team = models.ForeignKey(Team, verbose_name='Team')
