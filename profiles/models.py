from django.db import models
from django.contrib.auth.models import User


class UserProfileManager(models.Manager):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='User Profile', db_index=True)
    university = models.CharField(verbose_name='University', max_length=50, null=False, blank=False, db_index=True)
    profile_picture = models.ImageField(
        verbose_name='Profile Picture', upload_to='profile_pictures/', null=True, blank=True
    )

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'


class Team(models.Model):
    name = models.CharField(verbose_name='Team Name', max_length=20, null=False, blank=False, db_index=True)
    users = models.ManyToManyField(
        UserProfile, verbose_name='Team Users', through='UserTeam', through_fields=('team', 'user')
    )
    creation_date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class UserTeam(models.Model):
    team = models.ForeignKey(Team, verbose_name='Team')
    user = models.ForeignKey(UserProfile, verbose_name='User Profile')
