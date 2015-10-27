# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151027_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfr',
            name='supplier',
            field=models.ForeignKey(default=1, to='core.Supplier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='rfp',
            name='customer',
            field=models.ForeignKey(to='core.Customer'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
