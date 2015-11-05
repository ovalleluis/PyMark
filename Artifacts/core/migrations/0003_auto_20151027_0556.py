# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pfr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PfrResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid', models.CharField(max_length=200)),
                ('pfr', models.ForeignKey(to='core.Pfr')),
            ],
        ),
        migrations.CreateModel(
            name='Rfp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RfpRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ask', models.CharField(max_length=200)),
                ('rfp', models.ForeignKey(to='core.Rfp')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 5, 56, 2, 554057, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 5, 56, 16, 727758, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rfp',
            name='customer',
            field=models.OneToOneField(to='core.Customer'),
        ),
        migrations.AddField(
            model_name='pfrresponse',
            name='rfpRequirement',
            field=models.ForeignKey(to='core.RfpRequirement'),
        ),
        migrations.AddField(
            model_name='pfr',
            name='rfp',
            field=models.ForeignKey(to='core.Rfp'),
        ),
    ]
