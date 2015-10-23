# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_representative_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('company_zipcode', models.CharField(max_length=20)),
                ('company_phone', models.CharField(max_length=20)),
                ('company_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
