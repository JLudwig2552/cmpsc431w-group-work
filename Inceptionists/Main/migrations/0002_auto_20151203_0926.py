# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('addressid', models.AutoField(serialize=False, primary_key=True, db_column=b'addressID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)),
                ('streetaddr', models.CharField(max_length=255, db_column=b'streetAddr')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.DecimalField(max_digits=5, decimal_places=0)),
                ('zip_ext', models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)),
            ],
            options={
                'db_table': 'addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Auctions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
                ('reserve_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'auctions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bidderid', models.IntegerField(db_column=b'bidderID')),
                ('itemid', models.IntegerField(db_column=b'itemID')),
                ('timestamp', models.DateTimeField()),
                ('amount', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'bids',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=2000, null=True, blank=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creditcards',
            fields=[
                ('ccv', models.IntegerField()),
                ('merchant', models.CharField(max_length=20)),
                ('ccnumber', models.DecimalField(serialize=False, decimal_places=0, primary_key=True, db_column=b'ccNumber', max_digits=16)),
                ('exp_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'creditcards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('itemid', models.AutoField(serialize=False, primary_key=True, db_column=b'itemID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('content', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'ratings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('content', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'sells',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('itemct', models.IntegerField(db_column=b'itemCt')),
                ('carrier_trackingnum', models.CharField(max_length=255, null=True, db_column=b'carrier_trackingNum', blank=True)),
                ('saleprice', models.DecimalField(decimal_places=2, max_digits=6, db_column=b'salePrice')),
            ],
            options={
                'db_table': 'transactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True, db_column=b'userID')),
                ('user_type', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateTimeField()),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(to='Main.Categories'),
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('userid', models.ForeignKey(related_name='vendors_userid', primary_key=True, db_column=b'userID', serialize=False, to='Main.Users')),
                ('company_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vendors',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
