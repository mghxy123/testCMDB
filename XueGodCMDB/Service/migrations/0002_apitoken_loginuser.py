# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.CharField(verbose_name='token值', max_length=32)),
                ('time', models.DateTimeField(verbose_name='生成时间')),
                ('user_id', models.CharField(verbose_name='token用户', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=32)),
                ('password', models.CharField(verbose_name='密码', max_length=32)),
            ],
        ),
    ]
