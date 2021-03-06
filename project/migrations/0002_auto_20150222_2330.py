# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_auto_20150222_2330'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bodyFile',
            field=models.ForeignKey(related_name='readme', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filemanager.fileobject', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ForeignKey(related_name='thumbnail', on_delete=django.db.models.deletion.SET_DEFAULT, default=None, blank=True, to='filemanager.fileobject', null=True),
            preserve_default=True,
        ),
    ]
