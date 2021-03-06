# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0008_address_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='items',
            field=models.ManyToManyField(to='world.Item', blank=True),
        ),
    ]
