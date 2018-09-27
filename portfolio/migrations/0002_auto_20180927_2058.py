# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-27 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalimage',
            name='caption',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='journalimage',
            name='desc',
            field=models.TextField(default='***', max_length=500),
        ),
        migrations.AlterField(
            model_name='potraitimage',
            name='caption',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='potraitimage',
            name='desc',
            field=models.TextField(default='***', max_length=500),
        ),
        migrations.AlterField(
            model_name='stillimage',
            name='caption',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='stillimage',
            name='desc',
            field=models.TextField(default='***', max_length=500),
        ),
        migrations.AlterField(
            model_name='weddingimage',
            name='caption',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='weddingimage',
            name='desc',
            field=models.TextField(default='***', max_length=500),
        ),
    ]