# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='接口名称', max_length=32)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='接口描述')),
                ('doc', models.CharField(verbose_name='接口文档', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户账号', max_length=32)),
                ('password', models.CharField(verbose_name='用户密码', max_length=32)),
                ('nickname', models.CharField(verbose_name='用户姓名', max_length=32)),
                ('phone', models.CharField(verbose_name='用户手机号', max_length=32)),
                ('email', models.EmailField(verbose_name='用户邮箱', max_length=254)),
                ('photo', models.ImageField(verbose_name='用户头像', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(verbose_name='服务器ip', max_length=32)),
                ('mac', models.CharField(verbose_name='服务器物理地址', max_length=32)),
                ('cpu', models.CharField(verbose_name='服务器CPU', max_length=32)),
                ('memory', models.CharField(verbose_name='服务器内存', max_length=32)),
                ('disk', models.CharField(verbose_name='服务器磁盘', max_length=32)),
                ('isalive', models.CharField(verbose_name='服务器状态', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('service_id', models.IntegerField()),
                ('cpu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('service_id', models.IntegerField()),
                ('Memory_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cmdbuser',
            name='service',
            field=models.ManyToManyField(to='Service.Service'),
        ),
    ]
