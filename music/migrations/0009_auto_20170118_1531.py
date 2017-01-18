# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 07:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0008_song_total_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumLikeShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='albumlikeship',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
        migrations.AddField(
            model_name='albumlikeship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='liked_by',
            field=models.ManyToManyField(related_name='like_albums', through='music.AlbumLikeShip', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='albumlikeship',
            unique_together=set([('user', 'album')]),
        ),
    ]
