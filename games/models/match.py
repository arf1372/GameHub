from django.db import models

from games.models.game import Game
from profiles.models import Team


class Match(models.Model):
    game = models.ForeignKey(Game, verbose_name='Game')
    teams = models.ManyToManyField(Team, verbose_name='Team', through='TeamMatch', through_fields=('match', 'team'))
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    result = models.FileField(verbose_name='Result', upload_to='uploaded/results/', null=False, blank=False)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'


class TeamMatch(models.Model):
    match = models.ForeignKey(Match, verbose_name='Match')
    team = models.ForeignKey(Team, verbose_name='Team')
