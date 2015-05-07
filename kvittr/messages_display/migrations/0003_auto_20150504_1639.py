# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages_display', '0002_message_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='likes',
        ),
        migrations.AddField(
            model_name='message',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
