# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_num', models.IntegerField()),
                ('issue_description', models.CharField(max_length=10000)),
                ('uploaded_by', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
