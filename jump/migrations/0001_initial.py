# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-23 23:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('channel', models.CharField(editable=False, max_length=100, unique=True, verbose_name=b'Channel name')),
                ('log', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=b'Log name')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('width', models.PositiveIntegerField(default=90)),
                ('height', models.PositiveIntegerField(default=40)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'audit',
                'verbose_name': '\u64cd\u4f5c\u65e5\u5fd7',
                'verbose_name_plural': '\u64cd\u4f5c\u65e5\u5fd7',
                'permissions': (('can_delete_audit', '\u53ef\u4ee5\u5220\u9664\u64cd\u4f5c\u65e5\u5fd7'), ('can_view_audit', '\u53ef\u4ee5\u67e5\u770b\u64cd\u4f5c\u65e5\u5fd7'), ('can_play_audit', '\u53ef\u4ee5\u64ad\u653e\u64cd\u4f5c\u65e5\u5fd7')),
            },
        ),
    ]
