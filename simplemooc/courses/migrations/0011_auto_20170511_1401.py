# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_delete_teste'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
