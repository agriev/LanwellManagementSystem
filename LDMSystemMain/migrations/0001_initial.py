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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_assigned', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('item_ptr', models.OneToOneField(to='LDMSystemMain.Item', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=('LDMSystemMain.item', 'LDMSystemMain.executive'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('item_ptr', models.OneToOneField(to='LDMSystemMain.Item', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('experience', models.IntegerField(verbose_name='Опыт', default=0)),
                ('rating', models.IntegerField(verbose_name='Рейтинг', default=0)),
                ('description', models.TextField(verbose_name='Описание', default='')),
                ('phone', models.CharField(verbose_name='Телефон', default='', max_length=20)),
                ('email', models.EmailField(verbose_name='e-mail', default='', max_length=30)),
                ('executive_ptr', models.OneToOneField(to='LDMSystemMain.Executive', parent_link=True, auto_created=True)),
            ],
            options={
            },
            bases=('LDMSystemMain.item', 'LDMSystemMain.executive'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('item_ptr', models.OneToOneField(to='LDMSystemMain.Item', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=30)),
                ('description', models.CharField(verbose_name='Описание', max_length=30)),
            ],
            options={
            },
            bases=('LDMSystemMain.item',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('item_ptr', models.OneToOneField(to='LDMSystemMain.Item', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('datestart', models.DateTimeField(null=True, auto_now=True, verbose_name='Дата начала')),
                ('datefinish', models.DateTimeField(null=True, auto_now=True, verbose_name='Дата завершения')),
                ('duration', models.IntegerField()),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ASSIGNED', 'ASSIGNED'), ('IN_PROGRESS', 'IN PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELED', 'CANCELED')], default='NEW', max_length=20)),
                ('is_project', models.BooleanField(verbose_name='Является проектом', default=False)),
            ],
            options={
            },
            bases=('LDMSystemMain.item',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('task_ptr', models.OneToOneField(to='LDMSystemMain.Task', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=('LDMSystemMain.task',),
        ),
        migrations.AddField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(to='LDMSystemMain.Task', verbose_name='Родительская задача', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='person',
            field=models.ManyToManyField(to='LDMSystemMain.Executive', through='LDMSystemMain.Assigment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(to='LDMSystemMain.Skill', verbose_name='Навык', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='executive_ptr',
            field=models.OneToOneField(to='LDMSystemMain.Executive', parent_link=True, auto_created=True),
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
