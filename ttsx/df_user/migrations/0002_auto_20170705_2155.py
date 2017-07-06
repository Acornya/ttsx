# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr_detail',
            field=models.CharField(default=b'', max_length=80),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ucode',
            field=models.CharField(default=b'', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default=b'', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(default=b'', max_length=40),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='urcv',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
