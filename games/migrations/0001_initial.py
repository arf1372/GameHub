# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import games.models.code
import games.models.match


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('c', 'C'), ('cpp98', 'C++98'), ('cpp11', 'C++11'), ('cpp14', 'C++14'), ('java7', 'Java 7'), ('java8', 'Java 8'), ('py2', 'Python 2'), ('py3', 'Python 3')], max_length=5, verbose_name='Language')),
                ('file', models.FileField(upload_to=games.models.code.upload_path, verbose_name='File')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Code',
                'verbose_name_plural': 'Codes',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('result', models.FileField(upload_to=games.models.match.upload_path, verbose_name='Result')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game', verbose_name='Game')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Match', verbose_name='Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Team', verbose_name='Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(through='games.TeamMatch', to='profiles.Team', verbose_name='Team'),
        ),
    ]
