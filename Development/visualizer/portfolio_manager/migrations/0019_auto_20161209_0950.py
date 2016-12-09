# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_manager', '0018_auto_20161209_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedPersonDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_manager.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='projectmanagerdimension',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectmanagerdimension',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectmanagerdimension',
            name='value',
        ),
        migrations.RemoveField(
            model_name='projectownerdimension',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectownerdimension',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectownerdimension',
            name='value',
        ),
        migrations.AddField(
            model_name='projectmanagerdimension',
            name='associatedpersondimension_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_manager.AssociatedPersonDimension'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectownerdimension',
            name='associatedpersondimension_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_manager.AssociatedPersonDimension'),
            preserve_default=False,
        ),
    ]
