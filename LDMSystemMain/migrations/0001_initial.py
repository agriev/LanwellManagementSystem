# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assigment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_assigned', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('executive_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='LDMSystemMain.Item')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=('LDMSystemMain.item', 'LDMSystemMain.executive'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='LDMSystemMain.Item')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('executive_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='LDMSystemMain.Executive')),
            ],
            options={
            },
            bases=('LDMSystemMain.item', 'LDMSystemMain.executive'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='LDMSystemMain.Item')),
                ('name', models.CharField(max_length=30)),
                ('duration', models.IntegerField()),
                ('person', models.ManyToManyField(through='LDMSystemMain.Assigment', to='LDMSystemMain.Executive')),
            ],
            options={
            },
            bases=('LDMSystemMain.item',),
        ),
        migrations.AddField(
            model_name='company',
            name='executive_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, to='LDMSystemMain.Executive'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_item',
            field=models.ForeignKey(to='LDMSystemMain.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assigment',
            name='person',
            field=models.ForeignKey(to='LDMSystemMain.Executive'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assigment',
            name='task',
            field=models.ForeignKey(to='LDMSystemMain.Task'),
            preserve_default=True,
        ),
    ]
