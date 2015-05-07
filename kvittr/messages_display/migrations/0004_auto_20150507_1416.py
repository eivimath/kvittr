# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages_display', '0003_auto_20150504_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='points',
            new_name='likes',
        ),
    ]
