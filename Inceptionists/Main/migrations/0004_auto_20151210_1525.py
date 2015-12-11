# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20151203_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True, db_column=b'userID')),
                ('user_type', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateTimeField()),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='auctions',
            name='itemid',
            field=models.ForeignKey(db_column=b'itemID', default=2, to='Main.Items'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctions',
            name='auctioneerid',
            field=models.ForeignKey(db_column=b'auctioneerID', default=1, to='Main.User'),
            preserve_default=False,
        ),
    ]
