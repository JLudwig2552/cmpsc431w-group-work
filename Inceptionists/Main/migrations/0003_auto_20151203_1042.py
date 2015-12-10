# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20151203_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auctions',
            options={'managed': True},
        ),
    ]
