# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policedata',
            name='District_Sector',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='policedata',
            name='Zone_Beat',
            field=models.CharField(max_length=5),
        ),
    ]
