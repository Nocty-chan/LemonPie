# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumebuilder', '0012_auto_20170729_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupentrylinkedlist',
            name='cv_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cv_entry', to='resumebuilder.CVEntry'),
        ),
        migrations.AlterField(
            model_name='groupentrylinkedlist',
            name='predecessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='predecessor01', to='resumebuilder.GroupEntryLinkedList'),
        ),
        migrations.AlterField(
            model_name='groupentrylinkedlist',
            name='successor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='successor01', to='resumebuilder.GroupEntryLinkedList'),
        ),
    ]
